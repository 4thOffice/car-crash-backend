# Generated by Django 3.2.18 on 2023-06-27 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sketches', '0003_auto_20230627_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='sketchcar',
            name='car_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
