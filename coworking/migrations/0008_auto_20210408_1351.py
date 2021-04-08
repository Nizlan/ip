# Generated by Django 3.1.6 on 2021-04-08 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coworking', '0007_auto_20210408_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availabletime',
            name='days_for_regular2',
            field=models.CharField(max_length=150, verbose_name='Специальные дни'),
        ),
        migrations.AlterField(
            model_name='availabletime',
            name='is_round_the_clock',
            field=models.BooleanField(null=True, verbose_name='Круглосуточно'),
        ),
        migrations.AlterField(
            model_name='availabletime',
            name='regular_end',
            field=models.TimeField(null=True, verbose_name='Конец работы'),
        ),
        migrations.AlterField(
            model_name='availabletime',
            name='regular_end2',
            field=models.TimeField(null=True, verbose_name='Конец работы в специальные дни'),
        ),
        migrations.AlterField(
            model_name='availabletime',
            name='regular_start',
            field=models.TimeField(null=True, verbose_name='Начало работы'),
        ),
        migrations.AlterField(
            model_name='availabletime',
            name='regular_start2',
            field=models.TimeField(null=True, verbose_name='Начало работы в специальные дни'),
        ),
    ]