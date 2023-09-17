from rest_framework import viewsets

from subscription.models import Subscription
from subscription.serializers import SubscriptionSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def perform_create(self, serializer):

        subscription = serializer.save()
        subscription.user = self.request.user
        subscription.save()
