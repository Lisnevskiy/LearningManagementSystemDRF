from rest_framework import serializers

from payment.models import Payment
from payment.services import create_url_payment


class PaymentCreateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для создания платежа и получения URL для оплаты через Stripe Checkout.
    Позволяет создавать платежи и включает в себя поле 'payment_url' с URL для оплаты.
    Attributes:
        payment_url (str): Поле для хранения URL для оплаты.
    """
    payment_url = serializers.SerializerMethodField()

    class Meta:
        model = Payment
        fields = ('pk', 'user', 'course', 'lesson', 'payment_date', 'amount', 'payment_method', 'payment_url')

    def get_payment_url(self, obj):
        """
        Получает URL для оплаты на основе данных платежа и возвращает его.
        Args:
            obj (Payment): Объект платежа.
        Returns:
            str: URL для оплаты через Stripe Checkout.
        """
        amount_in_cents = int(obj.amount * 100)

        payment_data = {
            "amount": amount_in_cents,
        }

        if obj.course:
            payment_data['name'] = obj.course.title

        if obj.lesson:
            payment_data['name'] = obj.lesson.title

        payment_url = create_url_payment(payment_data)

        return payment_url


class PaymentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для вывода данных платежа.
    """
    class Meta:
        model = Payment
        fields = ('pk', 'user', 'course', 'lesson', 'payment_date', 'amount', 'payment_method')
