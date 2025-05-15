from django import forms
from .models import Article, Category
from django.contrib.auth.models import User

class ArticleForm(forms.ModelForm):
    new_category = forms.CharField(
        label="Otra categoría",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Escribe una nueva categoría',
            'style': 'display: none;'  # Oculto por defecto
        })
    )
    
    class Meta:
        model = Article
        fields = ['title', 'content', 'public', 'image', 'categories']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'public': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'categories': forms.SelectMultiple(attrs={
                'class': 'form-select',
                'id': 'id_categories'
            }),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Asegurarse de que el campo categories use el widget Select2
        self.fields['categories'].widget.attrs.update({'class': 'form-select'})
