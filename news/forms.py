from .models import Artiles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArtilesForm(ModelForm):
    class Meta:
        model = Artiles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Назва новини'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Анонс'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Дата публікації: 2000-01-01 00:00:00'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder' : 'Текст'
            }),

        }