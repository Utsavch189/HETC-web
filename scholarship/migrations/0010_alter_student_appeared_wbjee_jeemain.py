# Generated by Django 3.2.8 on 2022-04-10 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0009_alter_student_appeared_wbjee_jeemain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='appeared_wbjee_jeeMain',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
