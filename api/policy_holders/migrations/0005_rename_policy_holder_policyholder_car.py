# Generated by Django 3.2.18 on 2023-05-10 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('policy_holders', '0004_auto_20230510_1139'),
    ]

    operations = [
        migrations.RenameField(
            model_name='policyholder',
            old_name='policy_holder',
            new_name='car',
        ),
    ]