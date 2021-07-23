# Generated by Django 3.1.3 on 2021-03-11 11:21

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MSP', '0007_auto_20210310_2102'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repeating_weeks', models.IntegerField(default=1)),
                ('first_lesson_start', models.TimeField(default=datetime.time(9, 0))),
                ('lesson_length', models.TimeField(default=datetime.timedelta(seconds=5700))),
                ('break_length', models.TimeField(default=datetime.timedelta(seconds=900))),
                ('max_lessons', models.IntegerField(default=6)),
                ('theme', models.CharField(default='#FF81F2', max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='lesson',
            name='classroom',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='color',
            field=models.CharField(default='#FF81F2', max_length=200),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='start_time',
            field=models.TimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='type',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0)),
                ('start_time', models.TimeField(blank=True, default=django.utils.timezone.now)),
                ('end_time', models.TimeField(blank=True, default=django.utils.timezone.now)),
                ('settings', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MSP.settings')),
            ],
        ),
    ]
