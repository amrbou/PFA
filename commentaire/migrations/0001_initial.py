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
            name='Commentaire',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('texte', models.TextField()),
                ('notation', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('clientID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentaire_set', to='client.client')),
            ],
        ),
    ]
