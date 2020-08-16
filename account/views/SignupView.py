from account.serializers.SignUpSerializer import MarkRegisteredSerializer, SignUpSerializers,UserPersonalDetailsSerializer
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
    

class MarkRegistered(APIView):
    def post(self, request):
        client = razorpay.Client(auth=("rzp_test_GP7hCrPCLZN5V5", "WaGtzJA3vHOZRAHBAuHM8wbI"))
        payment_id = request.data.get('payment_id')
        resp=""
        try:
            resp = client.payment.fetch(payment_id)
        except Exception as e:
            return Response({"status":False, "msg":str(e)})
        if resp.get('status')=="captured":
            ser=MarkRegisteredSerializer(data=request.data)
            if ser.is_valid():
                if ser.validated_data['registered']:
                    user_instance=get_object_or_404(UserDetails,email=ser.validated_data['email'])
                    if not user_instance.registered:
                        user_instance.registered=True
                        user_instance.save()
                        return Response({"status":True, "registered":user_instance.registered, "msg":"Registered Successfully"})
                    
                    else:
                        print("firing response")
                        return Response({"status":False, "msg":"User Already Registered"})
                
                else:
                    return Response({"status":False, "msg":"Payment was unsuccessful"})
            else:
                return Response({"status": False, "msg":ser.errors})
        else:
            return Response({'status':False, "msg":"Payment Not Captured"})

        