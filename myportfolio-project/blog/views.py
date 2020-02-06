from django.shortcuts import render,get_object_or_404
from .models import Blog

def allblog(request):
    blogs=Blog.objects
    return render(request,'blog/allblog.html',{'blogs':blogs})

def detail(request,id_):
    detail_blog=get_object_or_404(Blog,pk=id_)
    return render(request,'blog/detail.html',{'detail_blog':detail_blog})
