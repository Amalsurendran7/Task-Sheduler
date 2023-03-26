from django.urls import path
from . import views

from django.views.generic.base import TemplateView


urlpatterns = [
               path('',TemplateView.as_view(template_name="frontend/login.html"),name='loginpage'),
        path('registerpage',TemplateView.as_view(template_name="frontend/Register.html"),name='registerpage'),
        # path('calendarpage/<int:id>',views.Calendar,name='calendarpage'),
      
    

]
