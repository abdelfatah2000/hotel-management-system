# Generated by Django 3.1.4 on 2021-01-04 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_booking_room_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='room_number',
        ),
    ]
