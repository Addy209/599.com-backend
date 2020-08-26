from account.models import UserDetails
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from account.serializers.BankSerializer import BankSerializers

class BankView(APIView):
    def post(self,request):
        email=request.data.get('email')
        user=get_object_or_404(UserDetails,email=email)
        ser=BankSerializers(data=request.data)
        if ser.is_valid():
            try:
                ser.save(user=user)
            except Exception as e:
                return Response({'status':False, 'msg':str(e)})
            else: 
                return Response({'status':True, 'msg':'Bank Details Saved Successfully'})
        else:
            return Response({'status':False, 'msg':ser.errors})