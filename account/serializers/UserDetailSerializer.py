from account.models import UserDetails
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    email=serializers.EmailField()
    name=serializers.SerializerMethodField()
    first_name=serializers.CharField(write_only=True)
    last_name=serializers.CharField(write_only=True)
    gender=serializers.CharField()
    father_name=serializers.CharField()
    mother_name=serializers.CharField()
    mobile=serializers.CharField()
    qualification=serializers.CharField()
    occupation=serializers.CharField()

    def get_name(self,obj):
        print(obj)
        return obj.get('first_name')+" "+obj.get('last_name')

