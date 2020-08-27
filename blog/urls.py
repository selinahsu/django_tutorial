from django.urls import path
# from "." means from current directory
from . import views 

urlpatterns = [
  # homepage is the home function inside views.py module
  path('', views.home, name='blog-home'), # name is like an id
  path('about/', views.about, name='blog-about'),
]