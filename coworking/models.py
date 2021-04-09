from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Place(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    location = models.TextField(verbose_name='Местоположение')
    price = models.FloatField(verbose_name='Цена за час, р')
    categories = models.ForeignKey('Categories', null=True, on_delete=models.PROTECT, verbose_name='Категория')
    services = models.ManyToManyField('Services')
    available_time = models.ForeignKey('AvailableTime', null=True, on_delete=models.PROTECT, verbose_name='Время работы')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class Categories(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Services(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class AvailableTime(models.Model):
    is_round_the_clock = models.BooleanField(null=True, verbose_name='Круглосуточно')
    regular_start = models.TimeField(null=True, verbose_name='Начало работы')
    regular_end = models.TimeField(null=True, verbose_name='Конец работы')
    regular_start2 = models.TimeField(null=True, verbose_name='Начало работы в специальные дни')
    regular_end2 = models.TimeField(null=True, verbose_name='Конец работы в специальные дни')
    days_for_regular2 = models.CharField(max_length=150, verbose_name='Специальные дни')

    def __str__(self):
        return f'{self.regular_start} - {self.regular_end}'

    class Meta:
        verbose_name = 'Время работы'
        verbose_name_plural = 'Времена работы'


class BookedTime(models.Model):
    start = models.TimeField(null=True, verbose_name='Начало работы')
    end = models.TimeField(null=True, verbose_name='Конец работы')
    place = models.ForeignKey('Place', null=True, on_delete=models.CASCADE, verbose_name='Место')
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.start} - {self.end}'

    class Meta:
        verbose_name = 'Забронированное время'
        verbose_name_plural = 'Забронированные часы'
