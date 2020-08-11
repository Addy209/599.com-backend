from account.serializers.OTPserializer import EMAIL_OTP_serializer,SMS_OTP_serializer,EmailOTPVerifySerializer,PhoneOTPVerifySerializer
from rest_framework import request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from account.models import *
from django.shortcuts import get_object_or_404
from django.conf import settings
import random

class OTP:

    @staticmethod
    def sendemailOTP(user):
        
        if user.is_active:
            raise Exception('User is already active')
        else:
            otp=OTP.gen_otp(99999,1000000)
            data={
                "otp":otp
            }
            print(data)
            old=""
            try:
                old=get_object_or_404(EMAIL_OTP,user=user)
            except Exception as e:
                print(e)
            print(old)
            if old:
                print(1)
                ser=EMAIL_OTP_serializer(old,data=data)
            else:
                print(2)
                ser=EMAIL_OTP_serializer(data=data)
            
            if ser.is_valid():  
                ser.save(user=user)
                print("OTP Saved")
            print(ser.errors)
            ####################################
            # Logic to generate and send Email #
            ####################################

    @staticmethod
    def sendsmsOTP(user):
        if user.is_active:
            raise Exception('User is already active')
        else:
            otp=OTP.gen_otp(999,10000)
            data={
                "otp":otp
            }
            print(otp)
            old=""
            try:
                old=get_object_or_404(SMS_OTP,user=user)
            except Exception as e:
                print(e)
            print(old)
            if old:
                print(1)
                ser=SMS_OTP_serializer(old,data=data)
            else:
                print(2)
                ser=SMS_OTP_serializer(data=data)
            
            if ser.is_valid():  
                ser.save(user=user)
                print("OTP Saved")
           ####################################
            # Logic to generate and send SMS #
            ####################################
    @staticmethod
    def try_to_activate_user(user):
        email_otp_instance=EMAIL_OTP.objects.get(user=user)
        phone_otp_instance=SMS_OTP.objects.get(user=user)
        if email_otp_instance.validated:
            if phone_otp_instance.validated:
                user.is_active=True
                user.save()
                return "User is activated successfully"
            else:
                return "Phone Number not Verified"
        else:
            return "Email Not Verified"

    @staticmethod
    def gen_otp(start,end):
        otp=random.randint(start,end)
        return otp

class EmailOTPVerify(APIView):
    def post(self, request):
        ser=EmailOTPVerifySerializer(data=request.data)
        if ser.is_valid():
            email=ser.validated_data['email']
            otp=ser.validated_data['otp']
            print(1)
            user=UserDetails.objects.get(email=email)
            print(2)
            email_otp_model_instance=EMAIL_OTP.objects.get(user=user)
            print(3)
            if not email_otp_model_instance.validated:
                if  email_otp_model_instance.otp==otp:
                    email_otp_model_instance.validated=True
                    email_otp_model_instance.save()
                    user_activated=OTP.try_to_activate_user(user)
                    return Response({"status":True, "msg":"Email Verified","account_status":user_activated})
                else:
                    return Response({"status":False, "msg":"Invalid OTP"})
            else:
                return Response({"status":False, "msg":"User Already Verified"})
        else:
            return Response({"status":False, "msg":"Invalid Data Provided"})


class SmsOTPVerify(APIView):
    def post(self, request):
        ser=PhoneOTPVerifySerializer(data=request.data)
        if ser.is_valid():
            mobile=ser.validated_data['phone']
            otp=ser.validated_data['otp']
            print(1)
            user=UserDetails.objects.get(mobile=mobile)
            print(2)
            phone_otp_model_instance=SMS_OTP.objects.get(user=user)
            print(3)
            if not phone_otp_model_instance.validated:
                if  phone_otp_model_instance.otp==otp:
                    phone_otp_model_instance.validated=True
                    phone_otp_model_instance.save()
                    user_activated=OTP.try_to_activate_user(user)
                    return Response({"status":True, "msg":"Phone Number Verified","account_status":user_activated})
                else:
                    return Response({"status":False, "msg":"Invalid OTP"})
            else:
                return Response({"status":False, "msg":"User Already Verified"})
        else:
            return Response({"status":False, "msg":"Invalid Data Provided","error":ser.errors})

