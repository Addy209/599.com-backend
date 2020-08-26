
from Transaction.serializers import TransactionSerializers
from utils.constants import razorpay_id, razorpay_pass
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from account.models import UserDetails
from account.serializers.SignUpSerializer import MarkRegisteredSerializer
from .models import TransactionDetails
import requests
import json
import razorpay
from razorpay import client

class CreateOrderNumber(APIView):

    def post(self, request):
        order_amount=request.data.get('amount')
        email=request.data.get('email')
        if order_amount=='registration':
            order_amount=599
        else:
            return Response({'status':False, "msg":"order amount keyword not valid"})

        data={
            'amount':order_amount*100,
            'currency':'INR',
            'payment_capture':'1'
        }
        resp=requests.post('https://api.razorpay.com/v1/orders', data, auth=(razorpay_id, razorpay_pass ))

        print(resp.text)

        jsonResp=json.loads(resp.text)
        print(jsonResp)
        if jsonResp.get('id') is not None:
            user=get_object_or_404(UserDetails,email=email)
            data={
                'user':user.id,
                'amount':order_amount,
                'order_number':jsonResp.get('id')
            }
            ser=TransactionSerializers(data=data)
            if ser.is_valid():
                ser.save()
                return Response({'status':True,'order':ser.validated_data['order_number']})
            else:
                return Response({'status':False, 'error':ser.errors,'msg':"Data Not Saved in Records"})
        else:
            return Response({'status':False,'msg':"Order not Created"})



            
    
    def put(self,request,pk):
        
        client = razorpay.Client(auth=(razorpay_id, razorpay_pass))
        payment_id = request.data.get('payment_id')
        resp=""
        try:
            resp = client.payment.fetch(payment_id)
        except Exception as e:
            return Response({"status":False, "msg":str(e)})
        if resp.get('status')=="captured":
            transaction_instance=get_object_or_404(TransactionDetails,pk=pk)
            if transaction_instance.status:
                return Response({"status":False, "msg": "Payment Already Captured for this order Id"})
            data={
                'payment_id':payment_id,
                'status':True
            }
            ser=TransactionSerializers(transaction_instance,data=data,partial=True)
            if ser.is_valid():
                ser.save()
            else:
                print("Payment successful but user record not saved")
            
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
