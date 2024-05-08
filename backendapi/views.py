from django.shortcuts import render
from rest_framework import generics
from todo.models import User
from .serilizer import Userserializer
# Create your views here.


class UserList(generics.ListCreateAPIView):
    result = User.objects.all()
    outputvalue = Userserializer

