from rest_framework import serializers

from payment.serializers import PaymentSerializer
from users.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    """
    Сериализатор для регистрации пользователя.
    """
    class Meta:
        model = User
        fields = ('pk', 'email', 'password')


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор основной информации о пользователе для модели User.
    """
    class Meta:
        model = User
        fields = ('pk', 'email', 'first_name', 'last_name', 'phone', 'city', 'avatar')


class UserOwnerDetailSerializer(serializers.ModelSerializer):
    """
    Сериализатор для детальной информации о пользователе для владельца профиля.
    """
    payment = PaymentSerializer(many=True, read_only=True)  # Сериализатор для поля payment, включая множество платежей

    class Meta:
        model = User
        fields = ('pk', 'email', 'first_name', 'last_name', 'phone', 'city', 'avatar', 'payment')


class UserDetailSerializer(serializers.ModelSerializer):
    """
    Сериализатор для детальной информации о пользователе для других пользователей.
    """
    class Meta:
        model = User
        fields = ('email', 'first_name', 'phone', 'city', 'avatar')
