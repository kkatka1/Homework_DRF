from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


from users.models import Payment, User


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
