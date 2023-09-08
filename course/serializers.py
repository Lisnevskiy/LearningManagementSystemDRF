from rest_framework import serializers
from course.models import Course
from lesson.models import Lesson


class CourseSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Course, который также включает количество уроков (lessons_count).
    """

    # Определение поля lessons_count с использованием SerializerMethodField
    lessons_count = serializers.SerializerMethodField()

    def get_lessons_count(self, obj):
        """
        Метод для получения количества уроков, связанных с данным курсом.
        Args:
            obj: Объект Course, для которого нужно получить количество уроков.
        Returns:
            int: Количество уроков для данного курса.
        """
        return Lesson.objects.filter(course=obj).count()

    class Meta:
        """
        Метакласс для определения модели, которая будет сериализована, и полей, включая lessons_count.
        """
        model = Course  # Указание модели Course
        fields = ('pk', 'title', 'description', 'image', 'lessons_count')
