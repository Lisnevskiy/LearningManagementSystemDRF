from django.urls import path

from payment.apps import PaymentConfig
from payment.views import *

app_name = PaymentConfig.name

urlpatterns = [
    path('', PaymentListView.as_view(), name='payments'),
    path('<int:pk>/', PaymentDetailView.as_view(), name='payments_detail'),
    path('create/', PaymentCreateView.as_view(), name='payments_create'),
    # path('update/<int:pk>/', PaymentUpdateView.as_view(), name='payments_update'),
    # path('delete/<int:pk>/', PaymentDeleteView.as_view(), name='payments_delete'),
]
