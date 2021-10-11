from django import forms
from django.forms import fields
from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('subject', 'name', 'description', 'body', 'pdf', 'video')
        widgets = {
            'subject': forms.Select(attrs={'class': "form-control"}),
            'name': forms.TextInput(attrs={'class': "form-control"}),
            'description': forms.TextInput(attrs={'class': "form-control"}),
            'body': forms.Textarea(attrs={'class': "form-control"})
        }