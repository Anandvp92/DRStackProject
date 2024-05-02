from typing import Any
from django import forms
from .models import User

class UserForm(forms.ModelForm):  
    password=forms.CharField(widget=forms.PasswordInput())  
    confirm_password=forms.CharField(widget=forms.PasswordInput())  
    class Meta:
        model= User
        fields=["first_name","last_name","phone_number","email","profile_pic","password"]
    def save(self,commit=True):
        newuser=super().save(commit=False)
        password= self.cleaned_data.get('password')
        newuser.set_password(password) 
        if commit:  
            newuser.save()
        return newuser
    
    
class LoginForm(forms.Form):
    email=forms.EmailField(label="Email")
    password=forms.CharField(label="Password",widget=forms.PasswordInput())


      

       