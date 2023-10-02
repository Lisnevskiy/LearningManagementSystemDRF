from django.db import models
from constants import NULLABLE
from course.models import Course
from lesson.models import Lesson
from users.models import User


class Payment(models.Model):
    """
    Модель для хранения информации о платежах пользователей за курсы или уроки.
    """

    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Наличные'),
        ('transfer', 'Перевод на счет'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='payment',  # Обратная связь для пользователя
        verbose_name='пользователь',
        **NULLABLE
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,  # Устанавливаем поле course в None при удалении курса
        **NULLABLE,
        related_name='payment',  # Обратная связь для курса
        verbose_name='оплаченный курс'
    )
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.SET_NULL,  # Устанавливаем поле lesson в None при удалении урока
        **NULLABLE,
        related_name='payment',  # Обратная связь для урока
        verbose_name='оплаченный урок'
    )
    payment_date = models.DateField(auto_now_add=True, verbose_name='дата оплаты')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, verbose_name='способ оплаты')
    payment_client_secret = models.CharField(
        max_length=100,
        verbose_name='секретный ключ платежа пользователя',
        **NULLABLE
    )

    def __str__(self):
        return f"Платеж от {self.user}"

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'
