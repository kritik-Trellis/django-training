from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def Signup(request):
    if (request.method=='POST'):
        if(request.POST['pass1']==request.POST['pass2']):
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request,'accounts/signup.html',{'error':'User Already Exist'})
            except User.DoesNotExist :
                user=User.objects.create_user(username=request.POST['username'] ,password=request.POST['pass1'])
                # auth.login(request,user)
                return redirect('home')
        else:
            return render(request,'accounts/signup.html',{'error':'Passwords do not match'})
    else:
        return render(request,'accounts/signup.html')

def Login(request):
    if(request.method=='POST'):
        user=auth.authenticate(username=request.POST['username'],password=request.POST['pass1'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'accounts/login.html',{'error':'Username or Password is Incorrect'})
    else:
        return render(request,'accounts/login.html')
def Logout(request):
    # if(request.method=="POST"):
    auth.logout(request)
    return redirect('home')
