from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone


def home(request):
    products=Product.objects
    return render(request,'products/home.html',{'products':products})
@login_required(login_url="/accounts/signup/")
def Create(request):
    if(request.method=='POST'):
        if(request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image'] ):
            product=Product()
            product.titles=request.POST['title']
            product.bodys=request.POST['body']
            if(request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://')):
                product.urls=request.POST['url']
            else:
                product.urls='https://'+request.POST['url']
            product.icons=request.FILES['icon']
            product.images=request.FILES['image']
            product.pub_dates=timezone.datetime.now()
            product.hunters=request.user
            product.save()
            return redirect('/products/'+ str(product.id))

        else:
            return render(request,'products/create.html',{'error':'All Fields Are Required'})
    else:
        return render(request,'products/create.html')


def detail(request,product_id):
    product=get_object_or_404(Product,pk=product_id)
    return render(request,'products/detail.html',{'product':product})


@login_required(login_url="/accounts/signup/")
def upvote(request,product_id):
    if(request.method=="POST"):
        product=get_object_or_404(Product,pk=product_id)
        product.votes_totals +=1
        product.save()
        return redirect('/products/'+str(product.id))

def search(request):
    product=Product.objects
    search_text=request.GET['q']
    status=product.filter(titles__icontains=search_text)
    if status :
        return render(request,'products/home.html',{'search_result':status})
    else:
        return render(request,'products/home.html',{'error':'Not Found'})
    
