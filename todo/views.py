from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
# Create your views here.


def list_todo(request):
    return HttpResponse("todo list")

def logging(request):
    if request.method=="POST":
        newuser=UserForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            return HttpResponse("User created")
    userform=UserForm()
    return render(request,"register.html",{"userform":userform})
