# Generated by Django 3.2.18 on 2023-05-12 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='registration_country',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='car',
            name='registration_plate',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
