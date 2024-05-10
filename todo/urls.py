from django.urls import path

from .views import Register,Loginuser,indexpage,logoutuser

urlpatterns=[
    path('register/',Register.as_view(),name="register"),
    path('login/',Loginuser,name="login"),
    path('index/',indexpage,name="index"),
    path('logout/',logoutuser,name="logout"),
]
