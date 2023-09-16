from rest_framework.routers import DefaultRouter

from subscription.apps import SubscriptionConfig
from subscription.views import SubscriptionViewSet

app_name = SubscriptionConfig.name

router = DefaultRouter()
router.register(r'subscriptions', SubscriptionViewSet, basename='subscriptions')
urlpatterns = router.urls
