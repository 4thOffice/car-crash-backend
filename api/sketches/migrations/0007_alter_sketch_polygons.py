# Generated by Django 3.2.18 on 2023-06-27 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sketches', '0006_alter_sketch_polygons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sketch',
            name='polygons',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
