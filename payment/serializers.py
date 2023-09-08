from rest_framework import serializers

from payment.models import Payment


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = ('pk', 'user', 'course', 'lesson', 'payment_date', 'amount', 'payment_method')
