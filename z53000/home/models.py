from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=200)
    published = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-published']

    def __str__(self):
        return f'{self.title} - {self.published}'


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
