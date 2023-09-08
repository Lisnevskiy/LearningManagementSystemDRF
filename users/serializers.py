from rest_framework import serializers

from payment.serializers import PaymentSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('pk', 'email', 'first_name', 'last_name', 'phone', 'city', 'avatar')


class UserDetailSerializer(serializers.ModelSerializer):

    payment = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('pk', 'email', 'first_name', 'last_name', 'phone', 'city', 'avatar', 'payment')
