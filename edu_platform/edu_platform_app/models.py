from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
	title = models.CharField(max_length=50)
	description = models.TextField(blank=True)
	price = models.IntegerField(null=True)
	group = models.IntegerField()
	link = models.CharField(max_length=100)

	def __str__(self):
		return self.title


class Teacher(models.Model):
	# своя модель тичера
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	description = models.TextField(blank=True)
	courses = models.ManyToManyField(Course, related_name='teachers')

	def __str__(self):
		return f'{self.user}'


class Lection(models.Model):
	title = models.CharField(max_length=50)
	description = models.TextField(blank=True)
	date = models.DateField()
	course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lections')

	def __str__(self):
		return f'{self.title}, {self.course}'


