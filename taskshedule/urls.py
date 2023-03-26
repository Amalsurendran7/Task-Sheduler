
from rest_framework import routers

from .views import TaskView,tasklist,getmydate
from django.urls import path
router=routers.DefaultRouter()
router.register('modelview',TaskView,basename='modelview')


urlpatterns = [

    path('task-list/',tasklist,name="tasklist"),
       path('getmydate/',getmydate,name="getmydate")
]
urlpatterns+=router.urls