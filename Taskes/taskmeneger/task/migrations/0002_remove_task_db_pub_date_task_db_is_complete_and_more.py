# Generated by Django 4.1.5 on 2023-02-01 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task_db',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='task_db',
            name='is_complete',
            field=models.BooleanField(default=False, verbose_name='Завершено'),
        ),
        migrations.AlterField(
            model_name='task_db',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название Задания'),
        ),
    ]
