from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from account.manager.manager import CustomUserManager
from django.db import models
from utils.constants import gender_choices,qualification_choices,occupation_choices
from django.conf import settings
import uuid

# Create your models here.

class UserDetails(AbstractBaseUser,PermissionsMixin):
    date_joined=models.DateTimeField(auto_now_add=True)
    email=models.EmailField(max_length=255, unique=True)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    gender=models.CharField(max_length=10,choices=gender_choices)
    father_name=models.CharField(max_length=255)
    mother_name=models.CharField(max_length=255)
    mobile=models.CharField(max_length=15, unique=True)
    qualification=models.CharField(max_length=25,choices=qualification_choices)
    occupation=models.CharField(max_length=25,choices=occupation_choices)
    registered=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)

    objects=CustomUserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['mobile']

    class Meta:
        app_label='account'

    def __str__(self) -> str:
        return self.email

    @property
    def get_full_name(self):
        return self.first_name+" "+self.last_name
    
    @property
    def get_short_name(self):
        return self.first_name

class UserPersonalDetails(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    pan=models.CharField(max_length=25, unique=True)
    aadhar=models.CharField(max_length=25, unique=True)

    def __str__(self) -> str:
        return self.user.get_full_name

class SMS_OTP(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    otp=models.IntegerField()
    validated=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.mobile+" "+str(self.otp)

class EMAIL_OTP(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    otp=models.IntegerField()
    validated=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.email+" "+str(self.otp)



    