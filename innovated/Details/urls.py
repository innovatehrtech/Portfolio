from django.urls import path 
from .import views

app_name='details'

urlpatterns = [
   
    path('contact/', views.contact_form, name='contact_form'),
]