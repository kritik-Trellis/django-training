from django.shortcuts import render
from .models import company

def home(request):
    jobs=company.objects.all()
    return render(request,'jobs/home.html',{'jobs':jobs})
