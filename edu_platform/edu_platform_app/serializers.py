from rest_framework.serializers import ModelSerializer
from .models import Course, Teacher, Lection
from django.contrib.auth.models import User


class LectionSerializer(ModelSerializer):
    class Meta:
        model = Lection
        fields = (
            'id',
            'title',
            'description',
            'date',
            'course'
        )


class LectionChildSerializer(ModelSerializer):
    class Meta:
        model = Lection
        fields = (
            'title',
            'description',
            'date',
        )


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name'
        )


class TeacherChildSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Teacher
        fields = (
            'user',
            'description'
        )


class TeacherSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Teacher
        fields = (
            'id',
            'user',
            'description'
        )


class CourseSerializer(ModelSerializer):
    lections = LectionChildSerializer(many=True)
    teachers = TeacherChildSerializer(many=True)

    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'description',
            'price',
            'group',
            'link',
            'lections',
            'teachers'
        )