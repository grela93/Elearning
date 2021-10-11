import random
from django.db import models
from course.models import Subject
from user.models import Student, Teacher

# Create your models here.

DIFF_CHOICES = {
    ('Dễ', 'Dễ'),
    ('Trung bình', 'Trung bình'),
    ('Khó', 'Khó')
}

RESULT_CHOICES = {
    ("Có", 'Có'),
    ("Không", 'Không')
}

class Quiz(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='quizzes')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='quizzes')
    name = models.CharField(max_length=255)
    number_of_question = models.IntegerField(default=0)
    time = models.IntegerField(help_text="Thời gian làm bài")
    required_score_to_pass = models.IntegerField(help_text="Điểm cần đạt")
    difficulity = models.CharField(max_length=10, choices=DIFF_CHOICES)
    show_result = models.CharField(max_length=10, choices=RESULT_CHOICES, default="Có")
    docx = models.FileField(upload_to='quiz', default='', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    def search(self):
        return f"{self.name} - {self.subject.name}"        

    def get_question(self):
        questions = list(self.questions.all())
        random.shuffle(questions)
        return questions[:self.number_of_question]


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=255)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        answers = list(self.answers.all()) # = return self.answer_set.all()
        random.shuffle(answers)
        return answers 


class Answer(models.Model):
    text = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"


class StudentAnswer(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='quiz_result')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='quiz_result')
    score = models.FloatField()

    def __str__(self):
        return f"{self.quiz.name} - {self.student.name}"