# Generated by Django 3.2.8 on 2022-04-11 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0014_detailsexam_total_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='user_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
