from django.contrib import admin
from .models import Teacher, Student

# Register your models here.

admin.site.register(Student)
admin.site.register(Teacher)