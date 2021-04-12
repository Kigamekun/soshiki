from django.shortcuts import render
from .models import Student,Teacher
# Create your views here.

def student(request):
	students = Student.objects.all()
	print(students)
	return render(request,'data/data_siswa.html',{'page_title':'Data Siswa','students':students})

def teacher(request):
	teachers = Teacher.objects.all()
	print(teachers)
	return render(request,'data/data_guru.html',{'page_title':'Data Guru','students':teachers})
