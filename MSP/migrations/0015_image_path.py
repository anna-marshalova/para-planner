# Generated by Django 3.1.3 on 2021-04-04 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MSP', '0014_auto_20210404_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='path',
            field=models.TextField(blank=True, null=True),
        ),
    ]
