# Generated by Django 3.1.6 on 2021-04-16 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20210416_2247'),
        ('coworking', '0006_auto_20210416_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='freeServices',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='services.freeservices', verbose_name='Бесплатные услуги'),
        ),
    ]
