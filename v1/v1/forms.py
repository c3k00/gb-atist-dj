from django import forms
from .models import Recipe, Category

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'instructions', 'prep_time', 'image', 'categories']
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'instructions': 'Шаги приготовления',
            'prep_time': 'Время приготовления (в минутах)',
            'image': 'Изображение',
            'categories': 'Категории',
        }
        widgets = {
            'instructions': forms.Textarea(attrs={'rows': 5}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']