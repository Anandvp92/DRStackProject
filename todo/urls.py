from django.urls import path
<<<<<<< HEAD
from .views import Register,Loginuser,indexpage,logoutuser

urlpatterns=[
    path('register/',Register.as_view(),name="register"),
    path('login/',Loginuser,name="login"),
    path('index/',indexpage,name="index"),
    path('logout/',logoutuser,name="logout"),
=======
from .views import List_Todo
urlpatterns=[
    path('logging/',List_Todo.as_view(),name="logging"),
>>>>>>> e97a5a59ca6659e535f211819299ac625db8d8e1
]