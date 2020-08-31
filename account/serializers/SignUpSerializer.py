from rest_framework import serializers
from rest_framework import fields
from account.models import UserDetails, UserPersonalDetails, UserRegistrationStatusDetails

class SignUpSerializers(serializers.ModelSerializer):
    class Meta:
        model=UserDetails
        exclude=('date_joined','is_staff','is_active')
        #fields=["email","password","first_name","last_name","gender","father_name","mother_name","mobile","qualification","occupation"]
    
class UserPersonalDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model=UserPersonalDetails
        fields=["pan","aadhar"]

class MarkRegisteredSerializer(serializers.Serializer):
    email=serializers.EmailField()
    registered=serializers.BooleanField()

class UserRegistrationStatusDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserRegistrationStatusDetails
        fields='__all__'