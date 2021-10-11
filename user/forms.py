from django import forms
from .models import Student, Teacher
 
 
class LoginForm(forms.Form):
    id = forms.CharField(max_length = 100)
    password = forms.CharField(widget = forms.PasswordInput())

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'avatar', 'school_year', 'gender', 'phone', 'email', 'address')
        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control"}),
            'school_year': forms.TextInput(attrs={'class': "form-control"}),
            'gender':forms.Select(attrs={'class': "form-control"}),
            'phone': forms.TextInput(attrs={'class': "form-control"}),
            'email': forms.TextInput(attrs={'class': "form-control"}),
            'address': forms.TextInput(attrs={'class': "form-control"}),
        }


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('name', 'avatar', 'gender', 'email')
        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control"}),
            'gender':forms.Select(attrs={'class': "form-control"}),
            'email': forms.EmailInput(attrs={'class': "form-control"}),
        }

