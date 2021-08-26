from django.db import models


class News(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=200)
    published = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-published']

    # def __str__(self):
    #     return f'{self.title} - {self.published}'


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Personal(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    master = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    sellary = models.FloatField()
    pidor = models.BooleanField()
    start_work_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Петушару'
        verbose_name_plural = 'Петушары'
        ordering = ['-start_work_date']


    def __str__(self):
        return f"{self.name[0]}.{self.surname}"
