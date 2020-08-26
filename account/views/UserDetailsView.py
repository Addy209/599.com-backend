from account.serializers.BankSerializer import BankSerializers
from account.serializers.UserDetailSerializer import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .OTPView import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class GetUserDetails(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user=request.user
        #print(user.__dict__)
        ser=UserSerializer(data=user.__dict__)
        bankdetails=get_object_or_404(UserBankDetails,user=user.id)
        bankser=BankSerializers(data=bankdetails.__dict__)
        if ser.is_valid() and bankser.is_valid():
            return Response({"status":True, "user":ser.data, "bank":bankser.data})
        else:
            return Response({"status":False, "error":bankser.errors})

class GetAncestorDetails(APIView):

    def get(self,request,pk):
        user=get_object_or_404(UserDetails,pk=pk)
        ser=UserSerializer(data=user.__dict__)
        bankdetails=get_object_or_404(UserBankDetails,user=user.id)
        bankser=BankSerializers(data=bankdetails.__dict__)
        if ser.is_valid() and bankser.is_valid():
            return Response({"status":True, "user":ser.data, "bank":bankser.data})
        else:
            return Response({"status":False, "error":ser.errors})