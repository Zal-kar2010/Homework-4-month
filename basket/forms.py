# basket/forms.py
from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        # Указываем поля, которые будут в форме
        fields = ['name', 'phone_number', 'card_number', 'status', 'book']