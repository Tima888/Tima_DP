from django import forms
from .models import Order
from django.forms import TextInput, DateTimeInput, Textarea

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'email', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),


            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'ПІБ'
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Email/Телефон/Telegram'
            }),
            "description": DateTimeInput(attrs={ 'rows': 4,
                'class': 'form-control',
                'placeholder' : 'Опис проблеми'
            }),


        }
