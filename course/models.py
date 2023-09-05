from django.db import models

from constants import NULLABLE


class Course(models.Model):
    title = models.CharField(max_length=300, verbose_name='название')
    description = models.TextField(verbose_name='содержание')
    image = models.ImageField(upload_to='course/', verbose_name='изображение', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
