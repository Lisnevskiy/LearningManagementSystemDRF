from django.db import models

from constants import NULLABLE


class Lesson(models.Model):
    title = models.CharField(max_length=300, verbose_name='название')
    description = models.TextField(verbose_name='содержание')
    image = models.ImageField(upload_to='lesson/', verbose_name='изображение', **NULLABLE)
    video_url = models.URLField(verbose_name='ссылка на видео', **NULLABLE)
    # video_link = models.CharField(max_length=200, verbose_name='ссылка на видео', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
