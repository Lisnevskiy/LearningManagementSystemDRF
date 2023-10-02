from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter

from payment.models import Payment
from payment.serializers import PaymentSerializer, PaymentCreateSerializer


class PaymentCreateView(generics.CreateAPIView):
    """
    Представление для создания нового платежа (Payment).
    """
    serializer_class = PaymentCreateSerializer


class PaymentListView(generics.ListAPIView):
    """
    Представление для вывода списка платежей с поддержкой фильтрации и сортировки.
    """
    queryset = Payment.objects.all()  # Запрос для получения всех платежей
    serializer_class = PaymentSerializer  # Сериализатор для преобразования данных платежей
    filter_backends = (DjangoFilterBackend, OrderingFilter,)  # Подключение фильтров и сортировки
    filterset_fields = ('course', 'lesson', 'payment_method')  # Поля для фильтрации
    ordering_fields = ('payment_date',)  # Поля для сортировки


class PaymentDetailView(generics.RetrieveAPIView):
    """
    Представление для вывода деталей платежа.
    """
    queryset = Payment.objects.all()  # Запрос для получения всех платежей
    serializer_class = PaymentSerializer  # Сериализатор для преобразования данных платежа
