# Generated by Django 3.2.18 on 2023-06-27 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sketches', '0004_sketchcar_car_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='polygon',
            name='sketch',
        ),
        migrations.AddField(
            model_name='sketch',
            name='polygons',
            field=models.JSONField(default=''),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='LatLng',
        ),
        migrations.DeleteModel(
            name='Polygon',
        ),
    ]
