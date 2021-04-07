from django.db import models

# Create your models here.


class Place(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    location = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'