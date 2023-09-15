from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import *

app_name = UsersConfig.name

urlpatterns = [
    path('', UserListView.as_view(), name='users'),
    path('<int:pk>/', UserDetailView.as_view(), name='users_detail'),
    path('create/', UserCreateView.as_view(), name='users_create'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='users_update'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='users_delete'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
