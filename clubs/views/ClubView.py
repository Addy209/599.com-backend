from rest_framework import request
from rest_framework.response import Response
from rest_framework.views import APIView
from clubs.serializers.clubSerializer import *
from django.shortcuts import  get_object_or_404
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
import requests
import json


class ClubView(APIView):

    def post(self,request):
        print("Hello")


        ser=ClubSerializer(data=request.data)
        print(ser)
        if ser.is_valid():
            try:
                ser.save()
            except Exception as e:
                print(str(e))
                return Response({"status":False, "msg":str(e)})
        else:
            return Response({"status":False, "msg":ser.errors})

        return Response({"status":True, "msg":"Tree Created Successfully"})

class GetClubDetailsView(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self, request):
        user=request.user
        club=Club.objects.get(user=user)
        print(club.__dict__)
        ser=GetClubDetailsSerializer(data=club.__dict__)
        if ser.is_valid():
            print(ser.data)
            parent,grandparent=None,None
            if ser.validated_data['grandparent_id']:
                gper=requests.get('https://fiveninitynine.herokuapp.com/account/getuserdetails/'+ser.validated_data['grandparent_id'])
                grandparent=json.loads(gper.text)
            if ser.validated_data['parent_id']:
                per=requests.get('https://fiveninitynine.herokuapp.com/account/getuserdetails/'+ser.validated_data['parent_id'])
                parent=json.loads(per.text)           
            
            return Response({"status":True, "parent":parent, 'grandparent':grandparent})
        else:
            return Response({"status":False, "msg":ser.errors})
