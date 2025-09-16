from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from captcha.fields import CaptchaField

class CustomUserCreationForm(UserCreationForm):
    phone = forms.CharField(max_length=15)
    address = forms.CharField(max_length=255)
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    education = forms.CharField(max_length=100)
    experience = forms.CharField(widget=forms.Textarea)
    skills = forms.CharField(widget=forms.Textarea)
    desired_position = forms.CharField(max_length=100)
    resume = forms.FileField(required=False)
    linkedin = forms.URLField(required=False)
    portfolio = forms.URLField(required=False)

    captcha = CaptchaField()

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = [
            "username", "email", "password1", "password2",
            "phone", "address", "birth_date", "education",
            "experience", "skills", "desired_position",
            "resume", "linkedin", "portfolio",
        ]
