# Generated by Django 3.2.8 on 2022-04-10 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0006_auto_20220410_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='created_at',
            field=models.DateField(null=True),
        ),
    ]
