# Generated by Django 3.1.3 on 2021-07-04 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MSP', '0050_settings_holidays'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='holidays',
        ),
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(default='2021-07-04')),
                ('end_date', models.DateField(default='2021-07-04')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='settings',
            name='holidays',
            field=models.ManyToManyField(blank=True, null=True, to='MSP.Holiday'),
        ),
    ]
