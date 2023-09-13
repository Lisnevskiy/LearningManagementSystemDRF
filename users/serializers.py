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


class UserDetailSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели User, предназначенный для вывода подробной информации о пользователе,
    включая информацию о платежах пользователя.
    """
    payment = PaymentSerializer(many=True, read_only=True)  # Сериализатор для поля payment, включая множество платежей

    class Meta:
        model = User
        fields = ('pk', 'email', 'first_name', 'last_name', 'phone', 'city', 'avatar', 'payment')
