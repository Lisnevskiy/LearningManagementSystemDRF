from django.db import models

from constants import NULLABLE
from course.models import Course
from users.models import User


class Subscription(models.Model):
    is_active = models.BooleanField(default=True, verbose_name='статус подписки')

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name='курс',
        related_name='subscription'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='пользователь',
        related_name='subscription',
        **NULLABLE
    )

    def __str__(self):
        return f"Подписка {self.user} на курс {self.course}"

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
