from rest_framework import serializers
from .models import *


class TaskSerializier(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields=['task','task_date','task_completed','user','id']
