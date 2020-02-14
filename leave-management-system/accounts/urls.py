from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home_login'),
    path('find_user/',views.find_user,name='find_user'),
    path('employee/',views.employee,name='employee'),
    path('manager/',views.manager,name='manager'),
    path('admin/',views.admin,name='admin'),
    path('logout/',views.logout,name="logout"),
    path('login/',views.login,name="login")
]
