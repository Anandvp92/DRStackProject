from typing import Any
from django import forms
from .models import User
class UserForm(forms.ModelForm):  
    password=forms.CharField(widget=forms.PasswordInput())  
    confirm_password=forms.CharField(widget=forms.PasswordInput())  
    class Meta:
        model= User
        fields=["first_name","last_name","phone_number","email","profile_pic"]

    def save(self, commit=False) -> Any:
        user = super().save(commit=False)
        password = self.cleaned_data.get("password")
        user.set_password(password)
        if not commit:
            user.save()
        return user
