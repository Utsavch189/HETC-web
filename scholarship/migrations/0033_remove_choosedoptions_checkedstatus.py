# Generated by Django 3.2.8 on 2022-04-24 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0032_auto_20220424_0735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choosedoptions',
            name='checkedStatus',
        ),
    ]
