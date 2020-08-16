from account.models import Transaction
from rest_framework import request
from rest_framework.response import Response
from rest_framework.views import APIView
from account.serializers.TransactionSerializer import TransactionSerializers
from account.decorators import GetUserFromPK
from django.shortcuts import get_object_or_404

class GetTransactionIdView(APIView):

    def put(self,request,pk):
        print(pk)
        status=request.data.get("paid")
        if status:
            instance=get_object_or_404(Transaction,pk=pk)
            ser=TransactionSerializers(instance,data=request.data,partial=True)
            if ser.is_valid():
                ser.save()
                return Response({"status":True})
            else:
                return Response({"status":False, "msg":ser.errors})
        else:
            return Response({"status":False})

    @staticmethod
    @GetUserFromPK
    def post(request):
        ser= TransactionSerializers(data=request)
        if ser.is_valid():
            obj=ser.save()
            print(obj.transaction_id)
            return Response({"status":True, "transaction_id":obj.transaction_id})
        else:
            return Response({"status":False, "msg":ser.errors})
        