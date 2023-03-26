from .models import *
from rest_framework import serializers
from taskshedule.serializers import *


class CustomUserSerializer(serializers.ModelSerializer):
    task=TaskSerializier(read_only=True,many=True)
    class Meta:
        model=CustomUser
        fields=['email','password','task','id','username']

class myserializer(serializers.Serializer) :
    task_date=serializers.DateField()
