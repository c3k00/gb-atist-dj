from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория рецепта'
        verbose_name_plural = 'Категории рецептов'


class Recipe(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    instructions = models.TextField(verbose_name='Шаги приготовления')
    prep_time = models.PositiveIntegerField(help_text="Время приготовления в минутах", verbose_name='Время приготовления')
    image = models.ImageField(upload_to='recipe_images/', verbose_name='Изображение', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    categories = models.ManyToManyField(Category, through='RecipeCategory', verbose_name='Категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name='Рецепт')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return f'{self.recipe.title} - {self.category.name}'

    class Meta:
        verbose_name = 'Связь Рецепт-Категория'
        verbose_name_plural = 'Связи Рецептов и Категорий'
