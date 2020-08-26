from rest_framework import serializers
from rest_framework import fields
from Transaction.models import TransactionDetails

class TransactionSerializers(serializers.ModelSerializer):
    class Meta:
        model=TransactionDetails
        fields='__all__'

