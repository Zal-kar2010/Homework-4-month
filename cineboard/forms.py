from django import forms
from .models import Films, Comment

class FilmsForm(forms.ModelForm):
    class Meta:
        model = Films
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']  # укажи только нужные поля
