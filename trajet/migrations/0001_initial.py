# Generated by Django 5.0.6 on 2024-06-19 14:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trajet',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('pointDepart', models.CharField(max_length=100)),
                ('pointArrivee', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('heure', models.TimeField()),
                ('IDClientConducteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trajets_conducteur', to='client.client')),
            ],
        ),
    ]
