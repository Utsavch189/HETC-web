# Generated by Django 3.2.8 on 2022-04-10 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0007_alter_student_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='created_at',
            field=models.DateField(),
        ),
    ]
