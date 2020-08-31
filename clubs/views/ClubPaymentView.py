from clubs.serializers.clubPaymentSerializer import GrandparentPaymentSerializer, ParentPaymentSerializer
from rest_framework import request
from clubs.models import Club, ClubPayment
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import cloudinary
from utils.constants import cloudinary_pass,cloudinary_id,cloud_name
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from clubs.permissions import IsRegistered


class GrandParentPaymentView(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated, IsRegistered]
    def post(self, request):
        club=get_object_or_404(Club,user=request.user)
        photo=request.FILES.get('screenshot')
        print(photo)
        cloudinary.config( 
        cloud_name = cloud_name, 
        api_key = cloudinary_id, 
        api_secret = cloudinary_pass 
        )
        resp=None
        try:
            resp=cloudinary.uploader.upload(photo, folder='Media/Payments/'+request.user.email+'/'+club.grandparent.email)
        except Exception as e:
            return Response({'status':False, 'error':str(e)})
        data=None
        try:
            data={
                'club':club.id,
                'grand_parent_paid':'pending',
                'grandparent_ss_url':resp['secure_url']
            }
        except  Exception as e:
            return Response({'status':False,"error":str(e),"msg":"Screenshot NOT Uploaded Successfully"})

        clubPayment=None
        try:
            clubPayment=get_object_or_404(ClubPayment, club=club)
        except Exception as e:
            pass
        ser=None
        if clubPayment:
            ser=GrandparentPaymentSerializer(instance=clubPayment,data=data,partial=True)
        else:
            ser=GrandparentPaymentSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return Response({'status':True, 'msg':'Screenshot Uploaded Successfully'})
        else:
            return Response({'status':False, 'error':ser.errors ,'msg':'Screenshot NOT Uploaded Successfully'})

class ParentPaymentView(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated, IsRegistered]
    def post(self, request):
        club=get_object_or_404(Club,user=request.user)
        photo=request.FILES.get('screenshot')
        print(photo)
        cloudinary.config( 
        cloud_name = cloud_name, 
        api_key = cloudinary_id, 
        api_secret = cloudinary_pass 
        )
        resp=None
        try:
            resp=cloudinary.uploader.upload(photo, folder='Media/Payments/'+request.user.email+'/'+club.parent.email)
        except Exception as e:
            return Response({'status':False, 'error':str(e)})
        data=None
        try:
            data={
                'club':club.id,
                'parent_paid':'pending',
                'parent_ss_url':resp['secure_url']
            }
        except  Exception as e:
            return Response({'status':False,"error":str(e),"msg":"Screenshot NOT Uploaded Successfully"})

        clubPayment=None
        try:
            clubPayment=get_object_or_404(ClubPayment, club=club)
        except Exception as e:
            pass
        ser=None
        if clubPayment:
            ser=ParentPaymentSerializer(instance=clubPayment,data=data,partial=True)
        else:
            ser=ParentPaymentSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return Response({'status':True, 'msg':'Screenshot Uploaded Successfully'})
        else:
            return Response({'status':False, 'error':ser.errors ,'msg':'Screenshot NOT Uploaded Successfully'})