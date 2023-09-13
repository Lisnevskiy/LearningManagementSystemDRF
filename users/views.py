from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import UserSerializer, UserDetailSerializer, UserRegisterSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class UserCreateView(generics.CreateAPIView):
    """
    Представление для создания нового пользователя.
    """
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        """
        Метод для создания нового пользователя с установленным паролем.
        Args:
            serializer: Сериализатор UserRegisterSerializer для сохранения данных пользователя.
        """
        password = self.request.data.get('password')  # Получение пароля из запроса
        user = serializer.save()  # Создание нового пользователя

        # Установка пароля для пользователя.
        # Пароль хэшируется перед сохранением.
        user.set_password(password)

        user.save()  # Сохраняем пользователя в базе данных


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
