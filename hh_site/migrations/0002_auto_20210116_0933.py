# Generated by Django 3.1.3 on 2021-01-16 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hh_site', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='work',
            field=models.CharField(max_length=30, unique=True, verbose_name='работа'),
        ),
    ]
