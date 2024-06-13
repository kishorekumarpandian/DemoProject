
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.home, name="home"),
    path("Signup",views.Signup, name="Signup"),
    path("Signin",views.Signin, name="Signin"),
    path("Signout",views.Signout, name="Signout"),
    
]
