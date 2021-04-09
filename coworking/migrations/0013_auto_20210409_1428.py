# Generated by Django 3.1.6 on 2021-04-09 11:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coworking', '0012_auto_20210408_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookedtime',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='place',
            name='price',
            field=models.FloatField(verbose_name='Цена за час, р'),
        ),
    ]
