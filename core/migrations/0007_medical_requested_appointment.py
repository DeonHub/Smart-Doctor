# Generated by Django 4.2.4 on 2023-08-28 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_appointment_rename_avatar_profile_profile_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='medical',
            name='requested_appointment',
            field=models.BooleanField(default=False),
        ),
    ]
