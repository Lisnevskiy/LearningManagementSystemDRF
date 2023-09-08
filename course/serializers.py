from rest_framework import serializers
from course.models import Course
from lesson.models import Lesson
from lesson.serializers import LessonSerializer


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
        model = Course
        fields = ('pk', 'title', 'description', 'image', 'lessons_count')


class CourseDetailSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Course с выводом связанных уроков.
    """

    # Определение поля lesson с использованием LessonSerializer для сериализации уроков.
    lesson = LessonSerializer(many=True, read_only=True)

    class Meta:
        """
        Метакласс для определения модели, которая будет сериализована, и полей, включая lesson.
        """
        model = Course
        fields = ('pk', 'title', 'description', 'image', 'lesson')
