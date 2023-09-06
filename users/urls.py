from django.urls import path

from users.apps import UsersConfig
from users.views import *

app_name = UsersConfig.name

urlpatterns = [
    path('', UserListView.as_view(), name='users'),
    path('<int:pk>/', UserDetailView.as_view(), name='users_detail'),
    path('create/', UserCreateView.as_view(), name='users_create'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='users_update'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='users_delete'),
]
