from django.db import models
from django.contrib.auth.models import User
from services.models import Equipment, UniqueQualities
# Create your models here.


class Place(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    location = models.TextField(verbose_name='Местоположение')
    price = models.FloatField(verbose_name='Цена за час, р')
    categories = models.ForeignKey('Categories', null=True, on_delete=models.DO_NOTHING, verbose_name='Категория')
    available_time = models.ForeignKey('AvailableTime', null=True, on_delete=models.DO_NOTHING, verbose_name='Время работы')
    equipment = models.ForeignKey('services.Equipment', null=True, verbose_name='Оснащение', on_delete=models.DO_NOTHING)
    uniqueQualities = models.ForeignKey('services.UniqueQualities', null=True,  verbose_name='Уникальные качества', on_delete=models.DO_NOTHING)
    freeServices = models.ForeignKey('services.FreeServices', null=True, verbose_name='Бесплатные услуги', on_delete=models.DO_NOTHING)

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
    start = models.TimeField(null=True, verbose_name='Начало')
    end = models.TimeField(null=True, verbose_name='Конец')
    place = models.ForeignKey('Place', null=True, verbose_name='Место', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.start} - {self.end}'

    class Meta:
        verbose_name = 'Забронированное время'
        verbose_name_plural = 'Забронированные часы'


class Reservation(models.Model):
    booked = models.ForeignKey('BookedTime', null=True, on_delete=models.PROTECT, verbose_name='Место')
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, verbose_name='Пользователь')

    def __str__(self):
        return f'{self.booked} - {self.user}'

    class Meta:
        verbose_name = 'Бронь'
        verbose_name_plural = 'Заказы на бронь'


class Comments(models.Model):
    text = models.TextField(verbose_name='Текст')
    place = models.ForeignKey('Place',  null=True, on_delete=models.DO_NOTHING, verbose_name='Место')
    user = models.ForeignKey(User, null=True, on_delete=models.PROTECT, verbose_name='ользователь')

    def __str__(self):
        return f'{self.place} - {self.user}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class GroupOfPeople(models.Model):
    people = models.ManyToManyField(User, null=True, verbose_name='Группа людей')

    def __str__(self):
        return self.people

    class Meta:
        verbose_name = 'Группа людей'
        verbose_name_plural = 'Группы людей'

