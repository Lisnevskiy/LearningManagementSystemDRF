from rest_framework import generics

from lesson.models import Lesson
from lesson.paginators import LessonSetPagination
from lesson.serializers import LessonSerializer
from users.permissions import IsOwner, IsStaff
from lesson.tasks import send_update_email


class LessonListView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsOwner | IsStaff]
    pagination_class = LessonSetPagination


class LessonDetailView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsOwner | IsStaff]


class LessonCreateView(generics.CreateAPIView):
    """
    Представление для создания нового урока (Lesson).
    """
    serializer_class = LessonSerializer

    def perform_create(self, serializer):
        """
        Метод выполняется при создании нового урока и делает текущего пользователя владельцем этого урока.
        """
        lesson = serializer.save()
        lesson.owner = self.request.user
        send_update_email.delay()
        lesson.save()


class LessonUpdateView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsOwner | IsStaff]


class LessonDeleteView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsOwner]
