from .models import *
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

def GetUserFromPK(func):
    def inner(*arg,**kwarg):
        request=arg[0]
        print(request.__dict__)
        #token=request.headers["Authorization"].split(" ")[1]
        email=request.data.get('email')
        amount=request.data.get('amount')
        user=get_object_or_404(UserDetails, email=email)
        print(user)
        if user:
            data={
                "user":user.id,
                "amount":amount
            }
            return func(data)
        else:
            return Response({"status":False, "msg":"Email not valid"})
    return inner