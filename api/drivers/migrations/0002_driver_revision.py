# Generated by Django 3.2.18 on 2023-04-28 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='revision',
            field=models.IntegerField(default=0),
        ),
    ]