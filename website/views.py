from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import signupform
# Create your views here.
def home(request):
    if request.method =='POST':
        us=request.POST["username"]
        pw=request.POST["password"]
        user=authenticate(request,username=us,password=pw)
        if user:
            login(request,user)
            messages.success(request,'Logged in successfully')
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

def register_user(request):
    if request.method=='POST':
        form=signupform(request.POST)
        if form.is_valid():
            form.save()
			# Authenticate and login
            username = form.cleaned_data['username']
            passW = form.cleaned_data['password1']
            # user = authenticate(username=username, password=passW)
            # login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
    else:
        form=signupform()
        return render(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':form})