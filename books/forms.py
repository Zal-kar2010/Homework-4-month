from django import forms
from .models import Review, TourRegistration

class ReviewForm(forms.ModelForm):
    RATING_CHOICES = [
        (1, '1 - Плохо'),
        (2, '2 - Неудовлетворительно'),
        (3, '3 - Удовлетворительно'),
        (4, '4 - Хорошо'),
        (5, '5 - Отлично')
    ]
    
    rating = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Оценка'
    )
    
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={
                'rows': 4, 
                'placeholder': 'Напишите ваш отзыв здесь...',
                'class': 'form-control'
            }),
        }
        labels = {
            'comment': 'Комментарий'
        }

class TourRegistrationForm(forms.ModelForm):
    class Meta:
        model = TourRegistration
        fields = ['participants', 'special_requests']
        widgets = {
            'participants': forms.NumberInput(attrs={
                'min': 1,
                'max': 10,
                'class': 'form-control',
                'style': 'width: 100px;'
            }),
            'special_requests': forms.Textarea(attrs={
                'rows': 3, 
                'placeholder': 'Ваши особые пожелания...',
                'class': 'form-control'
            })
        }
        labels = {
            'participants': 'Количество участников',
            'special_requests': 'Особые пожелания'
        }