from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserForm,LoginForm
from django.views import View
from .models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def Loginuser(request):
    if request.method=="POST":
        loginuser=LoginForm(request.POST)
        if loginuser.is_valid():
            password=loginuser.cleaned_data["password"]
            email=loginuser.cleaned_data["email"]
            user=authenticate(username=email,password=password)
            if user is not None:
                login(request,user)
                return redirect("index")
            else:
                loginuser=LoginForm(request.POST)  
                return redirect("login")          
            
    loginuser=LoginForm()
    return render(request,"login.html",{"userlogin":loginuser})


class Register(View):
    def post(self,request):
        userform=UserForm(request.POST,request.FILES)
        if userform.is_valid():
            userform.save()
            return HttpResponse("User created")
    def get(self,request):
        return render(request,'register.html',{'userform':UserForm()})
    
@login_required 
def indexpage(request):
    return render(request,'index.html',{})


def logoutuser(request):
    logout(request)
    return redirect('login')
    

    
    
    


