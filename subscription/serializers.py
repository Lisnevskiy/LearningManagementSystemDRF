from rest_framework import serializers

from subscription.models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = ('pk', 'is_active', 'course', 'user')
