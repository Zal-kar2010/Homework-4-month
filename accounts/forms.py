from django import forms
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField  # Используем django-simple-captcha
from .models import CustomUser

class MyForm(forms.Form):
    name = forms.CharField(max_length=100)
    captcha = CaptchaField()


class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=False)
    date_of_birth = forms.DateField(required=False)
    address = forms.CharField(max_length=255, required=False)
    education = forms.CharField(max_length=100, required=False)
    major = forms.CharField(max_length=100, required=False)
    work_experience = forms.CharField(widget=forms.Textarea, required=False)
    desired_salary = forms.DecimalField(required=False)
    skills = forms.CharField(widget=forms.Textarea, required=False)
    portfolio_url = forms.URLField(required=False)
    linkedin_url = forms.URLField(required=False)

    captcha = CaptchaField()  # Новая капча

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            'phone_number', 'date_of_birth', 'address', 'education',
            'major', 'work_experience', 'desired_salary', 'skills',
            'portfolio_url', 'linkedin_url',
        )

