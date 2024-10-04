from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from MyApp.models import *
#loginPage 
def loginPage(req):
    if req.method=="POST":
        user=authenticate(username=req.POST.get('username'),password=req.POST.get('password'))
        if user:
            login(req,user)
            return redirect('homePage')
        
        else:
            return HttpResponse(req,"You have don't account")


    return render(req,'loginPage.html')


#registerPage
def registerPage(req):
    if req.method=="POST":
        username=req.POST.get('username')
        password=req.POST.get('password')
        c_password=req.POST.get('c_password')
        email=req.POST.get('email')
        user_type=req.POST.get('user_type')

        if password==c_password:
            user=Custom_User_Model.objects.create_user(username=username,user_type=user_type,email=email,password=password)

            return redirect('loginPage')

    
    return render(req,'registerPage.html')


#homePage
def homePage(req):


    
    return render(req,'home.html')