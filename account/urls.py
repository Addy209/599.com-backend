from account.views.LoginView import LoginView
from account.views.OTPView import EmailOTPVerify, SmsOTPVerify
from django.contrib import admin
from django.urls import path, include
from account.views.SignupView import SignupView
from rest_framework.authtoken import views


urlpatterns = [
    path('signup/',SignupView.as_view()),
    path('otp/email/', EmailOTPVerify.as_view()),
    path('otp/sms/', SmsOTPVerify.as_view()),
    path('api-token-login/', LoginView.as_view())
]