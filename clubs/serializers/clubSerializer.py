from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from clubs.models import Club
from django.shortcuts import get_object_or_404
from account.models import UserDetails

class ClubSerializer(serializers.Serializer):
    parent=serializers.CharField()
    user=serializers.CharField()

    def get_id(self):
        return Club.objects.order_by('-id')[0].id+1

    def validate(self, attrs):
        print(attrs)
        parent=attrs['parent']
        print(parent)
        obj=""
        if parent.isnumeric():
            print("num found")
            obj=get_object_or_404(UserDetails,mobile=parent)
            print("found")
        else:
            obj=get_object_or_404(UserDetails,email=parent)
        attrs['parent']=obj

        user=attrs['user']
        print(user)
        if user.isnumeric():
            print("num found")
            obj=get_object_or_404(UserDetails,mobile=user)
            print("found")
        else:
            obj=get_object_or_404(UserDetails,email=user)
        attrs['user']=obj
        #attrs['id']=self.get_id()
        print(attrs)
        return attrs

    
    def save(self):
        print("Hello from save",self.validated_data['parent'])
        obj=get_object_or_404(Club,user=self.validated_data['parent'])
        
        if obj:
            if obj.parent:
                self.validated_data['grandparent']=obj.parent
            if not obj.l_child:
                obj.l_child=self.validated_data['user']
            elif not obj.r_child:
                obj.r_child=self.validated_data['user']
            else:
                raise Exception('Refered User has Already added two Users')
            obj.save()
        else:
            raise Exception('Refered User does not exist')

        clb=Club(**self.validated_data)
        clb.save()

class GetClubDetailsSerializer(serializers.Serializer):
    grandparent_id=serializers.CharField()
    parent_id=serializers.IntegerField()
        


