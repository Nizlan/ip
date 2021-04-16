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
