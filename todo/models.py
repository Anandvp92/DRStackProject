from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self,email,first_name,last_name,phone_number,password,**extrafield):
        if not email:
            raise ValueError("email is not valid")
        if not phone_number:
            raise ValueError("phone is not valid")
        email = self.normalize_email(email)
        extrafield.setdefault("is_staff",True)
        newuser= self.model(email=email,first_name=first_name,last_name=last_name,phone_number=phone_number,**extrafield)
        newuser.set_password(password)
        newuser.save()
        return newuser

    def create_superuser(self,email,first_name,last_name,phone_number,password=None,**extrafield):
        extrafield.setdefault("is_superuser",True)
        self.create_user(email=email,first_name=first_name,last_name=last_name,phone_number=phone_number,password=password,**extrafield)
        

class User(AbstractUser):

    username=None
    email=models.EmailField(unique=True)
    first_name=models.CharField(_("First Name"),max_length=250)
    last_name=models.CharField(_("Last Name"),max_length=20)
    last_login=models.DateTimeField(_("Last Login"),auto_now_add=True)
    phone_number=PhoneNumberField(_("Phone number"),unique=True)
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["first_name","last_name","phone_number"]
    objects= CustomUserManager()

    def __str__(self) -> str:
        return self.email
    
