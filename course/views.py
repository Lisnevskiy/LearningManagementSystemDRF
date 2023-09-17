from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from course.models import Course
from course.paginators import CourseSetPagination
from course.serializers import CourseSerializer, CourseDetailSerializer
from users.permissions import IsOwner


class CourseViewSet(viewsets.ModelViewSet):
    """
    Представление для модели Course, обеспечивающее CRUD-операции и настройку сериализатора.
    """
    queryset = Course.objects.all()  # Запрос к модели Course для получения данных
    pagination_class = CourseSetPagination

    def get_serializer_class(self):
        """
        Метод определяет класс сериализатора, используемый в зависимости от действия.
        Если выполняется действие 'retrieve' (просмотр одного курса), используется CourseDetailSerializer,
        иначе используется CourseSerializer.
        """
        if self.action == 'retrieve':
            return CourseDetailSerializer  # Используется при просмотре одного курса
        return CourseSerializer  # Используется для других действий (список, создание, обновление и удаление)

    def perform_create(self, serializer):
        """
        Метод выполняется при создании нового курса и делает текущего пользователя владельцем этого курса.
        """
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_permissions(self):
        """
        Метод определяет, какие разрешения применять в зависимости от действия в представлении.
        """
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsOwner]

        return [permission() for permission in permission_classes]
