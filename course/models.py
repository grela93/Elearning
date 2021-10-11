from django.db import models
from user.models import Teacher, Student

# Create your models here.

class Major(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default='', blank=True, null=True)

    def __str__(self):
        return self.name


class Subject(models.Model):
    major = models.ForeignKey(Major, on_delete=models.CASCADE, default='')
    name = models.CharField(max_length=100)
    description = models.TextField(default='', blank=True, null=True)

    def __str__(self):
        return self.name + " --- Thuộc ngành: " + self.major.name


class Course(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='courses')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')
    name = models.CharField(max_length=100)
    description = models.TextField(default='', blank=True, null=True)
    body = models.TextField(default='', blank=True, null=True)
    pdf = models.FileField(upload_to='pdf', default='', blank=True, null=True)
    video = models.FileField(upload_to='video', default='', blank=True, null=True)
    powerpoint = models.FileField(upload_to='powerpoint', default='', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' --- ' + self.teacher.name


class Comment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments', blank=True, null=True)
    body = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.course.name} --- {self.pk}"


class StudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='history_study')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='history_study')
    created_at = models.DateTimeField(auto_now_add=True)