from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=200)
    published = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-published']

    def __str__(self):
        return f'{self.title} - {self.published}'



