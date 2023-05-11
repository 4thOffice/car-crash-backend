# Generated by Django 3.2.18 on 2023-05-10 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_remove_car_policy_holder'),
        ('policy_holders', '0005_rename_policy_holder_policyholder_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='policyholder',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='policyholder',
            name='car',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='policy_holder', to='cars.car'),
        ),
    ]