# Generated by Django 3.2.8 on 2022-04-28 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0034_auto_20220426_0810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='author',
        ),
        migrations.RemoveField(
            model_name='result',
            name='exam_status',
        ),
        migrations.RemoveField(
            model_name='result',
            name='name',
        ),
    ]
