from rest_framework import fields
from account.models import Transaction
from rest_framework import serializers

class TransactionSerializers(serializers.ModelSerializer):
    class Meta():
        model=Transaction
        fields='__all__'

