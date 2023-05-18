# Generated by Django 3.2.18 on 2023-05-16 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crashes', '0002_auto_20230516_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crash',
            name='injuries',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='crash',
            name='other_material_damage',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='crash',
            name='vehicle_material_damage',
            field=models.BooleanField(default=False),
        ),
    ]
