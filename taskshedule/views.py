from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework import status
from  .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework.decorators import api_view
class TaskView(ModelViewSet):
    serializer_class=TaskSerializier
    permission_classes=(AllowAny,)
    http_method_names=['get','post','patch','delete']
    lookup_field = "id"

    def get_queryset(self):
        query=Task.objects.all()
        self.queryset=query
        return self.queryset
    
    def create(self,request,*args, **kwargs):
        # query=request.data['query']
        try:
        

            serializer=self.serializer_class(data=request.data)
            print(request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':serializer.data})
                           

            else:
                return Response({'failed':serializer.errors})
        except Exception as e:
              raise APIException(str(e))

        
    def update(self, request, pk=None, *args, **kwargs):
        # user = request.user
        instance = self.get_object()
        print(request.data,"first")
        data={key:value for key,value in request.data.items()  if request.data[key] != "default"}
        print(data,"changed")
        if request.data["task_completed"] == "completed":
            data["task_completed"]=True
        elif request.data["task_completed"] != "default":
            data["task_completed"]=False    
     
    
        serializer = self.serializer_class(instance=instance,
                                           data=data, # or request.data
                                        
                                           partial=True)
        if data:
                if serializer.is_valid():
                    serializer.save()
                    return Response({"msg":serializer.data})
                else:
                    return Response({"msg":serializer.errors})   

        else:
            return Response({"msg":"no updations"})         

    def destroy(self,request,*args, **kwargs):
        instance=self.get_object()     
        self.perform_destroy(instance)
        return Response({"msg":"task deleted"})
    def retrieve(self, request, *args, **kwargs):
        instance=Task.objects.all()
        page=self.paginate_queryset(instance)
        serializer=self.serializer_class(instance,many=True)

        return Response({'retreiving':serializer.data})
@api_view(['POST'])
def tasklist(request):
    user=request.data['id']
    print(user)
    user_obj=CustomUser.objects.get(id=user)
    task_obj=Task.objects.filter(user=user_obj)
    serializer=TaskSerializier(task_obj,many=True)
    print(serializer.data)
    return Response(serializer.data)
    
@api_view(['POST'])
def getmydate(request):
    userid=request.data["userid"]
    task_obj=Task.objects.filter(user=userid)
   
 
    serializer=TaskSerializier(task_obj,many=True)
 
    return Response({'tasks':serializer.data })
    
# Create your views here.
