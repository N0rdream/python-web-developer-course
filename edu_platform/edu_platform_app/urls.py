from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import (
    CourseViewSet,
    LectionViewSet,
    TeacherViewSet
)


router = DefaultRouter()

router.register(r'lections', LectionViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'teachers', TeacherViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]

