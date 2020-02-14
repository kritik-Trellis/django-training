from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .decorators import allowed_user
@allowed_user(allowed_roles=['admin','employee','bmanager'])
def home(request):
    return render(request,'accounts/home.html')

def login(request):
    return render(request,'accounts/login.html')

def find_user(request):
    if request.method=="POST":
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(request,username=email,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home_login')

            # if user.is_superuser:
            #     return redirect('admin')
            # if user.is_staff:
            #     return redirect('manager')
            # if user.is_active:
            #     return redirect('employee')
        else:
            return render(request,'accounts/login.html',{'error':'Enter a valid Email ID/Password'})
# @allowed_user(allowed_roles=['admin'])
def admin(request):
    # if request.user.is_authenticated:
    return render(request,'accounts/homepage.html',{'user_admin':'admin'})
    # else:
    #     return redirect('home')
# @allowed_user(allowed_roles=['bmanager'])
def manager(request):
    return render(request,'accounts/homepage.html',{'user_manager':'manager'})
    # else:
    #     return redirect('home')
# @allowed_user(allowed_roles=['employee'])
def employee(request):
    return render(request,'accounts/homepage.html',{'user_employee':'employee'})
    # else:
    #     return redirect('home')

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        # return redirect('home_login')
        return redirect('login')
