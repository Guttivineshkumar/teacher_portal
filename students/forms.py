from django import forms
from .models import Student, Teacher
from django.contrib.auth.forms import AuthenticationForm


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "subject", "score"]
