from account.views.OTPView import OTP
from account.serializers.LoginSerializer import Login_Serializer
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from account.models import *
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from django.conf import settings

class LoginView(ObtainAuthToken):

    def post(self,request):
        print(0)
        ser=Login_Serializer(data=request.data)
        if ser.is_valid():
            email=ser.validated_data['email']
            password=ser.validated_data['password']
            user=authenticate(username=email,password=password)
            if user:
                if user.is_active:
                    #if user.registered:
                    token,created=Token.objects.get_or_create(user=user)
                    print(1)
                    return Response({"status":True, "token":token.key,"registered":user.registered, 'grandparent_paid':user.grandparent_paid,'parent_paid':user.parent_paid})
                    # else:   
                    #     return Response({"status":False,"registered":user.registered,"msg":"User Has not paid registration amount!"})
                        
                else:
                    # OTP.sendemailOTP(user)
                    # OTP.sendsmsOTP(user)
                    # print(2)
                    return Response({"status":False,"msg":"User Not Acitve"})
            else:
                print(3)
                return Response({"status":False, "msg":"Wrong Email or Password"})
            
