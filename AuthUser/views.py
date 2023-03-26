from rest_framework import permissions
from  rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from  .models import *
from rest_framework.renderers import *
import uuid
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework.views import APIView
from .Serializers import *
from django.contrib.auth import authenticate,login
from  .utils.Email import send_email
from rest_framework.generics import RetrieveAPIView
from rest_framework.decorators import api_view
from taskshedule.models import *
from taskshedule.serializers import TaskSerializier
class UserDetail(RetrieveAPIView):
    """
    A view that returns a templated HTML representation of a given user.
    """
    queryset = CustomUser.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    lookup_field="id"
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer=CustomUserSerializer(self.object)
        return Response({'user':serializer.data }, template_name='frontend/task.html')

class Calendar(RetrieveAPIView):
    """
    A view that returns a templated HTML representation of a given user.
    """
    queryset = CustomUser.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    lookup_field="id"
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        task_date=[]
        task_obj=Task.objects.filter(user=self.object.id)
        for i in task_obj:
             task_date.append(i.task_date)
       
        output_dates = [d.strftime('%Y-%m-%d') for d in task_date]    
        serializer=TaskSerializier(task_obj,many=True)
        print(output_dates)
        return Response({'user':self.object.id,'tasks':serializer.data }, template_name='frontend/calendar.html')
    
class RegisterViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.IsAuthenticated(),)
        if self.request.method == 'POST':
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated())
    
    def create(self, request):
        '''
        When you create an object using the serializer\'s .save() method, the
        object\'s attributes are set literally. This means that a user registering with
        the password \'password\' will have their password stored as \'password\'. This is bad
        for a couple of reasons: 1) Storing passwords in plain text is a massive security
        issue. 2) Django hashes and salts passwords before comparing them, so the user
        wouldn\'t be able to log in using \'password\' as their password.
        We solve this problem by overriding the .create() method for this viewset and
        using Account.objects.create_user() to create the Account object.
        '''
        serializer = self.serializer_class(data=request.data,partial=True)
        email=request.data["email"]
        print(email)
        check=CustomUser.objects.filter(email=email)
        print(check)
        if serializer.is_valid() and not check :
            password = serializer.validated_data['password']
            confirm_password = password
            if password and confirm_password and password == confirm_password:
                user = CustomUser.objects.create_user(**serializer.validated_data)
                user.password=serializer.validated_data['password']
                user.otp=uuid.uuid4()

                user.save()
                return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        else:    
            print(serializer.is_valid())
            return Response({'status': serializer.errors,
                            'message': 'Account could not be created with received data.'
                            }, status=status.HTTP_400_BAD_REQUEST)
class LoginViewSet(APIView):
    permission_classes=(permissions.AllowAny,)
    
    def post(self, request, format=None):
    
     
            username = request.data['username']
            password = request.data['password']
            print(username,password)
            # if not request.user.is_anonymous():
            #     return Response('Already Logged-in', status=status.HTTP_403_FORBIDDEN)
            try:
                user = CustomUser.objects.get(username=username, password=password)
                print(user.id,"gr")

                if user is not None:
                        

                        return Response({"message":"success","id":user.id})
                        
            except:
                    return Response({'message':'Username/password combination invalid.'})
        
class OtpLogin(APIView):


    def post(self,request):
        email=request.data['email']
        try:
           check=CustomUser.objects.get(email=email)
        #    print(check)
          
           send_email(check.email,check.otp)
           request.session['email']=check.email
           serializer=CustomUserSerializer(check)
           return Response({"message":"otp send","user_data":serializer.data['email']})
        except  :
            return Response("you are not an active user,please register first ")

@api_view(['POST'])
def otpverify(request):
     otp=request.data['otp']
     email=request.data['email']
     print(otp)
     print(type(otp))
     print(email)
     try:
         check=CustomUser.objects.get(email=email)
         if check.otp == uuid.UUID(otp):
              return Response({"message":"success","id":check.id})
         else:
              return Response({"message":"not matching"})
     except:
          return Response({"message":"invalid otp"})    
     

