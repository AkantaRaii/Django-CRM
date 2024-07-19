from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import signupform,edit_form
from . import models
# Create your views here.
def home(request):
    records=models.Record.objects.all()
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
        return render(request,'home.html',{'records':records})
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

def show_record(request,pk):
    if request.user.is_authenticated:
        customer=models.Record.objects.get(id=pk)
        return render(request,'record.html',{'customer':customer})
    else:
        messages.success(request,"you are not logged in.Please login ")
        return redirect('home')
def edit(request,pk):
    if request.user.is_authenticated:
        current_record=models.Record.objects.get(id=pk)
        form=edit_form(request.POST,instance=current_record)
        if form.is_valid():
            form.save() 
            messages.success(request,"Edited Successfully")
            return redirect('home')
        form2=edit_form(None,instance=current_record)
        return render(request,'edit.html',{'form':form2})
    else:
        return redirect('home')
def delete(request,pk):
    pass