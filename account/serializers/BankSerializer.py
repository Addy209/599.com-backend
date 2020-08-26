from rest_framework import serializers
from rest_framework import fields
from account.models import UserBankDetails

class BankSerializers(serializers.ModelSerializer):
    class Meta:
        model=UserBankDetails
        fields=['bank_name','branch_name','ifsc_code','account_holder_name','account_number']
