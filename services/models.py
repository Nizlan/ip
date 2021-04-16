from django.db import models

# Create your models here.


class FreeServices(models.Model):
    free_tea = models.BooleanField(verbose_name="Бесплатный чай")
    free_wifi = models.BooleanField(verbose_name="Бесплатный wi-fi")
    parking_spaces = models.BooleanField(verbose_name="Свободные парковочные места")

    def __str__(self):
        return self.free_tea

    class Meta:
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуги'


class Equipment(models.Model):
    area = models.FloatField(verbose_name="Площадь, м2")
    free_spaces = models.IntegerField(verbose_name="Количество свободных мест")
    conference_hall = models.BooleanField(verbose_name="Наличие конференц зала")

    def __str__(self):
        return self.area

    class Meta:
        verbose_name = 'Оснащение'
        verbose_name_plural = 'Оснащения'


class UniqueQualities(models.Model):
    quality = models.CharField(max_length=150, verbose_name="Качество")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.quality

    class Meta:
        verbose_name = 'Уникальное качество'
        verbose_name_plural = 'Уникальные качества'
