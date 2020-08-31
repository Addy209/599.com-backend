from account.views.BankView import BankView
from account.views.UserDetailsView import GetAncestorDetails, GetUserDetails
from account.views.LoginView import LoginView
from account.views.OTPView import EmailOTPVerify, SmsOTPVerify
from django.contrib import admin
from django.urls import path, include
from account.views.SignupView import SignupView, UserPaymentView
from rest_framework.authtoken import views


urlpatterns = [
    path('signup/',SignupView.as_view()),
    path('bankdetails/',BankView.as_view()),
    #path('otp/email/', EmailOTPVerify.as_view()),
    #path('otp/sms/', SmsOTPVerify.as_view()),
    path('api-token-login/', LoginView.as_view()),
    path('getuserdetails/', GetUserDetails.as_view()),
    path('getuserdetails/<int:pk>', GetAncestorDetails.as_view()),
    path('submitpaymentss/', UserPaymentView.as_view()),
    # path('gettransactionordernumber/', GetTransactionIdView.as_view()),
    # path('gettransactionordernumber/<str:pk>', GetTransactionIdView.as_view()),
]