from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from app.forms import LoginForm, SignupForm
from django.contrib.auth import authenticate,login

# Create your views here.
def signuppage(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your account has been created! now you are able to log in')
            return redirect("loginpage")
        else:
            messages.error(request,"Request Error")
    else:
        form = SignupForm()
    return render(request,"signup.html",{'form':form})

def loginpage(request):
    if request.method == "POST":
        form = LoginForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect("homepage")
    else:
        form = LoginForm()
    return render(request,'login.html',{'form':form})

def homepage(request):

    return render(request,"home.html")