from rest_framework import serializers
# from rest_framework.relations import SlugRelatedField

# from course.models import Course
from lesson.models import Lesson


class LessonSerializer(serializers.ModelSerializer):

    # SlugRelatedField используется для представления поля course как строки (title),
    # а не как объекта Course, и запрос для queryset настроен на Course.objects.all()
    # course = SlugRelatedField(slug_field='title', queryset=Course.objects.all())

    class Meta:
        model = Lesson
        fields = ('pk', 'title', 'description', 'image', 'video_url', 'course', 'owner')
