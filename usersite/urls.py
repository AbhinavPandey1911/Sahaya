from django.contrib import admin
from django.urls import path
from usersite import views
urlpatterns = [
    path("",views.index,name='index'),
    path("myadmin_login",views.myadmin_login,name='myadmin_login'),
    path("SupportersLogin",views.SupportersLogin, name='SupportersLogin'),
    path("UsersLogin",views.UsersLogin, name='UsersLogin'),
    path("usersignup",views.usersignup, name='usersignup'),
    path("supsignup",views.supsignup, name='supsignup'),
    path("userhome",views.userhome, name='userhome'),
    path("supphome",views.supphome, name='supphome'),
    path("logout",views.index, name='index'),
]
