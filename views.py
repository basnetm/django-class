from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from .models import product,contacts
from math import ceil

# Create your views here.
def index(request):
    #return HttpResponse("manoj basnet")
    
    return render(request,'index.html')

def login(request):
    #return HttpResponse("manoj basnet")
    if request.method=='POST':
        username=request.POST['user']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            return redirect('/')
        else:
            messages.info(request,"username incorrect")
            return redirect('login')
    
    return render(request,'login.html')

def signup(request):
    #return HttpResponse("manoj basnet")
    if request.method=='POST':
        name=request.POST['user']
        print(name)
        email=request.POST['email']
        password=request.POST['password']
        repeat=request.POST['repeat']
        if password!=repeat:
            messages.warning(request,"password not matched")
            return redirect('signup')
        user=User.objects.create_user(
            username=name,
            email=email,
            password=password,
        )
        user.save()
       
        messages.success(request,"successed")
        return redirect('login')
    return render(request,'signup.html')

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        # print(name)
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']

        Contact1=contacts(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )
        Contact1.save()
        return redirect('contact')


    return render(request,'contact.html')


#to derive the item from the databse to homepage
#cats=category,catproduct=categoryproduct
#ceil=floring & celing ,params=parameter

def  index(request):
    allprods=[]
    catprods=product.objects.values('category','id')
    cats={item['category']for item in catprods}
    print(cats)
    for cat in cats:
        prod=product.objects.filter(category=cat)
        n=len(prod)
        nSlides=n//4 + ceil((n/4)-(n//4))
        allprods.append([prod,range(1,nSlides),nSlides])
    params={'allprods':allprods}
    return render(request,'index.html',params)