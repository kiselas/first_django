from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anonse', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Название статьи'
            }),
            'anonse': TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Анонс статьи'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата и время в формате ХХХХ-ХХ-ХХ ХХ:ХХ'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Полный текст'
            }),
        }