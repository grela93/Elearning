from django.contrib import admin
from .models import Quiz, Question, Answer, StudentAnswer

class AnswerInLine(admin.TabularInline):
    model = Answer

class QuestionDetail(admin.ModelAdmin):
    search_fields = ['text']
    inlines = [AnswerInLine]

class QuestionInLine(admin.TabularInline):
    model = Question

class ScoreInLine(admin.TabularInline):
    model = StudentAnswer

class QuizDetail(admin.ModelAdmin):
    list_display = ['name', 'subject_id', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']
    inlines = [QuestionInLine, ScoreInLine]

admin.site.register(Quiz, QuizDetail)
admin.site.register(Question, QuestionDetail)
admin.site.register(Answer)
admin.site.register(StudentAnswer)