from rest_framework import request
from rest_framework.response import Response
from rest_framework.views import APIView
from clubs.serializers.clubSerializer import *
from django.shortcuts import  get_object_or_404
from django.conf import settings

class ClubView(APIView):

    def post(self,request):
        print("Hello")


        ser=ClubSerializer(data=request.data)
        print(ser)
        if ser.is_valid():
            ser.save()
        else:
            print(ser.errors)

        return Response({"status":True, "msg":"Tree Created Successfully"})