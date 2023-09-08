from rest_framework import viewsets
from course.models import Course
from course.serializers import CourseSerializer, CourseDetailSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    Представление для модели Course, обеспечивающее CRUD-операции и настройку сериализатора.
    """
    queryset = Course.objects.all()  # Запрос к модели Course для получения данных

    def get_serializer_class(self):
        """
        Метод определяет класс сериализатора, используемый в зависимости от действия.
        Если выполняется действие 'retrieve' (просмотр одного курса), используется CourseDetailSerializer,
        иначе используется CourseSerializer.
        """
        if self.action == 'retrieve':
            return CourseDetailSerializer  # Используется при просмотре одного курса
        return CourseSerializer  # Используется для других действий (список, создание, обновление и удаление)
