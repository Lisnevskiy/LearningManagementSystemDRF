from django.db import models

from constants import NULLABLE
from course.models import Course
from users.models import User


class Lesson(models.Model):
    title = models.CharField(max_length=300, verbose_name='название')
    description = models.TextField(verbose_name='содержание')
    image = models.ImageField(upload_to='lesson/', verbose_name='изображение', **NULLABLE)
    video_url = models.URLField(verbose_name='ссылка на видео', **NULLABLE)
    # video_link = models.CharField(max_length=200, verbose_name='ссылка на видео', **NULLABLE)

    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', related_name='lesson')

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='владелец')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
