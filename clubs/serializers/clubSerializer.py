from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from clubs.models import Club
from django.shortcuts import get_object_or_404
from account.models import UserDetails
import re
from rest_framework.response import Response
from django.core.exceptions import ValidationError

Phone_re="^[6-9][0-9]{9}$"
Email_re="^[a-zA-Z][a-zA-Z0-9.-_]{2,150}@[a-zA-Z0-9]{2,50}.[a-zA-Z]{2,5}$"


class ClubSerializer(serializers.Serializer):
    parent=serializers.CharField()
    user=serializers.CharField()

    def get_id(self):
        return Club.objects.order_by('-id')[0].id+1
    
    def checkForAttribute(self,value,parameter):
        if parameter=='mobile':
            x=re.search(Phone_re,value)
            if not x:
                raise ValidationError('Phone Number is not Valid')
        
        elif parameter=='email':
            x=re.search(Email_re,value)
            if not x:
                raise ValidationError('Email is not Valid')
        

    def validate(self, attrs):
        print(attrs)
        parent=attrs['parent']
        print(parent)
        obj=""
        if parent.isnumeric():
            
            self.checkForAttribute(parent,'mobile')
            obj=get_object_or_404(UserDetails,mobile=parent)
            print("found")
        else:
            
            self.checkForAttribute(parent,'email')
            obj=get_object_or_404(UserDetails,email=parent)
        attrs['parent']=obj

        user=attrs['user']
        print(user)
        if user.isnumeric():
            
            self.checkForAttribute(user,'mobile')
            obj=get_object_or_404(UserDetails,mobile=user)
            print("found")
        else:
            
            self.checkForAttribute(user,'email')
            obj=get_object_or_404(UserDetails,email=user)
        attrs['user']=obj
        #attrs['id']=self.get_id()
        print(attrs)
        return attrs

    
    def save(self):
        print("Hello from save",self.validated_data['parent'])
        user_obj,obj=None,None
        try:
            obj=get_object_or_404(Club,user=self.validated_data['parent'])
            user_obj=get_object_or_404(Club,user=self.validated_data['user'])
        except Exception as e:
            pass


        if user_obj and obj:
            print(user_obj.id,obj.id)
            if user_obj.id<obj.id:
                raise Exception('Can not add this user as child to this parent.')
        print(obj)
        if obj:
            if obj.parent:
                self.validated_data['grandparent']=obj.parent
            if not obj.l_child:
                obj.l_child=self.validated_data['user']
            elif not obj.r_child:
                if obj.l_child==self.validated_data['user']:
                    raise Exception("Refered User has already added this user")
                obj.r_child=self.validated_data['user']
            else:
                raise Exception('Refered User has Already added two Users')
            obj.save()
        else:
            raise Exception('Refered User does not exist')
        

        clb=Club(**self.validated_data)
        clb.save()

class GetClubDetailsSerializer(serializers.Serializer):
    grandparent_id=serializers.CharField(required=False,allow_null=True)
    parent_id=serializers.CharField(required=False,allow_null=True)
    
        


