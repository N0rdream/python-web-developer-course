from django.contrib import admin
from .models import Course, Teacher, Lection


admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Lection)
