from django.urls import path,include
from .views import *
from django.views.decorators.csrf import csrf_exempt

from rest_framework import routers

router=routers.DefaultRouter()
router.register('registeruser',RegisterViewSet,basename='registeruser')

urlpatterns = [
    path('loginview',LoginViewSet.as_view(),name='loginview'),
     path('otpview',OtpLogin.as_view(),name='otpview'),
     path('userdetail/<int:id>/',UserDetail.as_view(),name="userdetail"),
        path('calendar/<int:id>/',Calendar.as_view(),name="calendar"),
        path('otpverify/',otpverify,name="otpverify")
]

urlpatterns+=router.urls