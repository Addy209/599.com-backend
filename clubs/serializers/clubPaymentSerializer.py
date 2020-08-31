from rest_framework import fields
from clubs.models import ClubPayment
from rest_framework import serializers

class GrandparentPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=ClubPayment
        fields=['club','grand_parent_paid','grandparent_ss_url']

class ParentPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=ClubPayment
        fields=['club','parent_paid','parent_ss_url']