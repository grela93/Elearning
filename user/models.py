from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.


class Student(models.Model):
    gender_choice = (("Nữ", "Nữ"), ("Nam", "Nam"), ("Khác", "Khác"))
    student = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    avatar = models.ImageField(upload_to='img', default='')
    name = models.CharField(max_length=50)
    school_year = models.CharField(max_length=100, default='')
    gender = models.CharField(max_length=20, choices=gender_choice)
    address = models.CharField(max_length=100, default='', blank=True, null=True)
    email = models.CharField(max_length=100, default='')
    phone = models.CharField(default='', max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    gender_choice = (("Nữ", "Nữ"), ("Nam", "Nam"), ("Khác", "Khác"))
    teacher = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher')
    major = models.ForeignKey("course.Major", on_delete=models.CASCADE, related_name='teacher')
    avatar = models.ImageField(upload_to='img', default='')
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=20, choices=gender_choice)
    email = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name + '  ---  Thuộc khoa: ' + self.major.name
