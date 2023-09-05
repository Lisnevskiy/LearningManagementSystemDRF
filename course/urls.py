from rest_framework.routers import DefaultRouter

from course.apps import CourseConfig
from course.views import CourseViewSet

app_name = CourseConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')
urlpatterns = router.urls
