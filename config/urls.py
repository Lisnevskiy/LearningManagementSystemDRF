from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('course.urls', namespace='course')),
    path('lessons/', include('lesson.urls', namespace='lesson')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
