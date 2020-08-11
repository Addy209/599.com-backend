from rest_framework.fields import EmailField
from account.models import EMAIL_OTP, SMS_OTP
from rest_framework import serializers


class SMS_OTP_serializer(serializers.ModelSerializer):
    class Meta:
        model=SMS_OTP
        fields=['otp']


class EMAIL_OTP_serializer(serializers.ModelSerializer):
    class Meta:
        model=EMAIL_OTP
        fields=['otp']

class EmailOTPVerifySerializer(serializers.Serializer):
    email=serializers.EmailField()
    otp=serializers.IntegerField()

class PhoneOTPVerifySerializer(serializers.Serializer):
    phone=serializers.RegexField("[6-9][0-9]{9}")
    otp=serializers.IntegerField()
