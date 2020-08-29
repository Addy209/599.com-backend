from account.serializers.SignUpSerializer import SignUpSerializers,UserPersonalDetailsSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .OTPView import *
import razorpay

class SignupView(APIView):
    def post(self,request):
        user_details=SignUpSerializers(data=request.data)
        personal_details=UserPersonalDetailsSerializer(data=request.data)
        if user_details.is_valid():

            user=user_details.save()
            user.set_password(user.password)
            user.save()

            if personal_details.is_valid():

                personal_details.save(user=user)
                #OTP.sendemailOTP(user)
                #OTP.sendsmsOTP(user)
                return Response({"status":True,"msg":"User Created!"}) #; To activate your account please verify the OTP
            else:
                return Response({"error":personal_details.error})

        
        else:
            print(user_details.errors)
            return Response({"error":user_details.errors}, status=500)
