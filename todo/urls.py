from django.urls import path
from .views import List_Todo
urlpatterns=[
    path('logging/',List_Todo.as_view(),name="logging"),
]