from django.urls import path
from .views import list_todo
urlpatterns=[
    path('listtodo/',list_todo,name="list_todo"),
]