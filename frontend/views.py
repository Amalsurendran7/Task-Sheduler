from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
# Create your views here.
from rest_framework.generics import RetrieveAPIView
from AuthUser.models import *
