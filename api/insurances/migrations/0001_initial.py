# Generated by Django 3.2.18 on 2023-06-26 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('revision', models.IntegerField(default=0)),
                ('state', models.CharField(choices=[('E', 'Empty'), ('P', 'Partial'), ('V', 'Validated')], default='E', max_length=1)),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('policy_number', models.CharField(blank=True, max_length=256, null=True)),
                ('agent', models.CharField(blank=True, max_length=256, null=True)),
                ('green_card', models.CharField(blank=True, max_length=256, null=True)),
                ('valid_until', models.DateTimeField(blank=True, null=True)),
                ('damage_insured', models.BooleanField(blank=True, null=True)),
                ('car', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='insurance', serialize=False, to='cars.car')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
