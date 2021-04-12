from django.db import models
from django.db import connections
# Create your models here.
class Student(models.Model):
	FirstName = models.CharField(max_length=255)
	LastName = models.CharField(max_length=255)
	
	Age = models.IntegerField()
	Nik = models.IntegerField()
	Kelas = models.CharField(max_length=10)
	class Meta:
		db_table = "students"

class Teacher(models.Model):
	FirstName = models.CharField(max_length=255)
	LastName = models.CharField(max_length=255)
	
	Age = models.IntegerField()
	Nip = models.IntegerField()
	expertClass = models.CharField(max_length=255)
	class Meta:
		db_table = "teachers"
