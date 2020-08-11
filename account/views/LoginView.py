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
            user=get_object_or_404(UserDetails,email=email)
            if user:
                if user.is_active:
                    password=ser.validated_data['password']
                    user=authenticate(username=email,password=password)
                    if user:
                        token,created=Token.objects.get_or_create(user=user)
                        print(1)
                        return Response({"status":True, "token":token.key,"registed":user.registered})
                    else:
                        return Response({"status":False, "msg":"Wrong Password"})
                else:
                    OTP.sendemailOTP(user)
                    OTP.sendsmsOTP(user)
                    print(2)
                    return Response({"status":False,"msg":"User Not Verified"})
            else:
                print(3)
                return Response({"status":False,"msg":"Unknown User"})
            
