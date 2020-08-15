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
        if ser.is_valid():
            return Response({"status":True, "user":ser.data})
        else:
            return Response({"status":False, "error":ser.errors})