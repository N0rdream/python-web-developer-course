from rest_framework.viewsets import ModelViewSet
from .models import Course, Teacher, Lection
from .permissions import IsSuperuserOrReadOnly
from .serializers import (
	CourseSerializer,
	TeacherSerializer,
	LectionSerializer
)


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsSuperuserOrReadOnly]


class LectionViewSet(ModelViewSet):
    queryset = Lection.objects.all()
    serializer_class = LectionSerializer
    permission_classes = [IsSuperuserOrReadOnly]


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsSuperuserOrReadOnly]