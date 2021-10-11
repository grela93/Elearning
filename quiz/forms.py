from django import forms
from .models import Quiz
 
class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['docx']
        widgets = {
            'docx': forms.FileInput(attrs={'class': "form-control"}),
        }