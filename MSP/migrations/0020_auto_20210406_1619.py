# Generated by Django 3.1.3 on 2021-04-06 09:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MSP', '0019_auto_20210406_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
    ]
