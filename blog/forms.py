from django import forms
from .models import Article, Category
from django.contrib.auth.models import User

class ArticleForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    
    class Meta:
        model = Article
        fields = ['title', 'content', 'public', 'image', 'categories']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'public': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
