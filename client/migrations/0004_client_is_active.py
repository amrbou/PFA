# Generated by Django 5.0.6 on 2024-06-28 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_client_phone_client_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
