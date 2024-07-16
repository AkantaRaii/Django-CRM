from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method =='POST':
        us=request.POST["username"]
        pw=request.POST["password"]
        user=authenticate(request,username=us,password=pw)
        if user:
            login(request,user)
            messages.success(request,"Logged in successfully")
            return redirect('home')
        else:
            messages.success(request,"username or password didnt match!!")
            return redirect('home')
    else:
        return render(request,'home.html')
def logout_user(request):
    logout(request)
    messages.success(request,"logged out")
    return redirect('home')