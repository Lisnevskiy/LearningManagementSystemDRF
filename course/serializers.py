from rest_framework import serializers
from course.models import Course
from lesson.models import Lesson
from lesson.serializers import LessonSerializer


class IsSubscribedMixin(serializers.Serializer):
    """
    Миксин для определения статуса подписки текущего пользователя на курс.
    """
    # Определение поля is_subscribed с использованием SerializerMethodField
    is_subscribed = serializers.SerializerMethodField()

    def get_is_subscribed(self, obj):
        """
        Метод для определения статуса подписки текущего пользователя на данный курс.
        Args:
            obj: Объект Course, для которого нужно определить статус подписки.
        Returns:
            bool: True, если пользователь подписан на курс, иначе False.
        """
        request = self.context.get('request')
        if request:
            # Проверяем, подписан ли текущий пользователь на данный курс
            return obj.subscription.filter(user=request.user).exists()
        return False  # Если пользователь не подписан


class CourseSerializer(IsSubscribedMixin, serializers.ModelSerializer):
    """
    Сериализатор для модели Course, который также включает количество уроков (lessons_count)
    и статус подписки пользователя на данный курс (is_subscribed).
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
        Метакласс для определения модели, которая будет сериализована, и полей, включая lessons_count и is_subscribed.
        """
        model = Course
        fields = ('pk', 'title', 'description', 'image', 'owner', 'lessons_count', 'is_subscribed')


class CourseDetailSerializer(IsSubscribedMixin, serializers.ModelSerializer):
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
        fields = ('pk', 'title', 'description', 'image', 'is_subscribed', 'lesson', 'owner')
