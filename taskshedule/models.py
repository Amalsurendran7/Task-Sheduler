from django.db import models
from django.utils import timezone
from AuthUser.models import *
# Create your models here.
class Task(models.Model):
     task_created= models.DateTimeField(default=timezone.now)
     task=models.TextField()
     task_date= models.DateField(auto_now_add=False)
     task_completed=models.BooleanField(default=False)
     user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='task')
     
     # def __str__(self):
     #      return self.task+self.id