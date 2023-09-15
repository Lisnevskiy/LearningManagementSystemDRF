from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.models import User
from users.permissions import IsUser
from users.serializers import UserSerializer, UserDetailSerializer, UserRegisterSerializer, UserOwnerDetailSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    """
    Представление для просмотра подробной информации о пользователе.
    """
    queryset = User.objects.all()

    def get_serializer_class(self):
        """
        Метод для определения класса сериализатора в зависимости от текущего пользователя.
        Returns:
            class: Класс сериализатора, который будет использоваться для этого запроса.
        """
        user = self.get_object()
        if self.request.user == user:
            return UserOwnerDetailSerializer
        return UserDetailSerializer


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
    permission_classes = [IsUser]


class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsUser]
