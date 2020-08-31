from utils.constants import cloud_name, cloudinary_id, cloudinary_pass
from account.serializers.SignUpSerializer import SignUpSerializers,UserPersonalDetailsSerializer, UserRegistrationStatusDetailsSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .OTPView import *
import cloudinary

class SignupView(APIView):
    def post(self,request):
        user_details=SignUpSerializers(data=request.data)
        personal_details=UserPersonalDetailsSerializer(data=request.data)
        if user_details.is_valid():

            user=user_details.save()
            user.set_password(user.password)
            

            if personal_details.is_valid():
                user.save()
                personal_details.save(user=user)
                #OTP.sendemailOTP(user)
                #OTP.sendsmsOTP(user)
                return Response({"status":True,"msg":"User Created!"}) #; To activate your account please verify the OTP
            else:
                return Response({"error":personal_details.error})

        
        else:
            print(user_details.errors)
            return Response({"error":user_details.errors}, status=500)

class UserPaymentView(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def post(self, request):
        photo=request.FILES.get('screenshot')
        print(photo)
        cloud=cloudinary.config( 
        cloud_name = cloud_name, 
        api_key = cloudinary_id, 
        api_secret = cloudinary_pass 
        )
        resp=cloudinary.uploader.upload(photo, folder='Media/registration/'+request.user.email)
        data=None
        try:
            data={
                'user':request.user.id,
                'payment_status':'pending',
                'ss_url':resp['secure_url']
            }
        except  Exception as e:
            return Response({'status':False,"error":str(e),"msg":"Screenshot NOT Uploaded Successfully"})
        ser=UserRegistrationStatusDetailsSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return Response({'status':True,"msg":"Screenshot Uploaded Successfully"})
        else:
            return Response({'status':False,"msg":"Screenshot NOT Uploaded Successfully"})
