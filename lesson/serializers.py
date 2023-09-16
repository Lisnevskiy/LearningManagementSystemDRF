from rest_framework import serializers

from lesson.models import Lesson
from lesson.validators import validate_lesson_links


class LessonSerializer(serializers.ModelSerializer):

    # Используется пользовательский валидатор для проверки ссылок на видеоресурсы урока.
    video_url = serializers.URLField(validators=[validate_lesson_links])

    class Meta:
        model = Lesson
        fields = ('pk', 'title', 'description', 'image', 'video_url', 'course', 'owner')
