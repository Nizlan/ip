from django.db import models

# Create your models here.


class Place(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    location = models.TextField(verbose_name='Местоположение')
    price = models.FloatField(verbose_name='Цена, р')
    # category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Название категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


# class Services(models.Model):
#     title = models.CharField(max_length=150, db_index=True, verbose_name='Название категории', default='null')
