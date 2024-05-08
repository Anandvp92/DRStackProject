from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
from django import views
# Create your views here.


class List_Todo(views.View):

    def get(self,request):
        userform=UserForm()
        return render (request,"register.html",{"userform":userform})
    
    def post(self,request):
        newuser=UserForm(request.POST,request.FILES)
        if newuser.is_valid():            
            newuser.save(commit=False)
            return  HttpResponse("User created")
        else:
            user_form = UserForm() 
            return render(request, "register.html", {"userform": user_form})
        

# def logging(request):
#     if request.method=="POST":
#         newuser=UserForm(request.POST)
#         if newuser.is_valid():
#             newuser.save()
#     userform=UserForm()
#     return render(request,"register.html",{"userform":userform})
