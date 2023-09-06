from django.urls import path

from lesson.apps import LessonConfig
from lesson.views import *

app_name = LessonConfig.name

urlpatterns = [
    path('', LessonListView.as_view(), name='lessons'),
    path('<int:pk>/', LessonDetailView.as_view(), name='lessons_detail'),
    path('create/', LessonCreateView.as_view(), name='lessons_create'),
    path('update/<int:pk>/', LessonUpdateView.as_view(), name='lessons_update'),
    path('delete/<int:pk>/', LessonDeleteView.as_view(), name='lessons_delete'),
]
