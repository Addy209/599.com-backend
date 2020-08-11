from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class Login_Serializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField()