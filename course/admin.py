from django.contrib import admin
from .models import Major, Subject, Course, Comment
from quiz.models import Quiz

admin.site.site_header = 'E Learning ADMIN'
# Register your models here.

class CommentInLine(admin.TabularInline):
    model = Comment
class CourseDetail(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']
    inlines = [CommentInLine]

class QuizInLine(admin.TabularInline):
    model = Quiz
class SubjectDetail(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']
    inlines = [QuizInLine]

admin.site.register(Major)
admin.site.register(Subject, SubjectDetail)
admin.site.register(Course, CourseDetail)
admin.site.register(Comment)
