# Generated by Django 3.1.4 on 2021-01-14 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_remove_booking_room_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='category',
            field=models.CharField(choices=[('Conditioner', 'Conditioner'), ('Non-Conditioner', 'Non-Conditioner'), ('Deluxe', 'Deluxe Rooom'), ('Single', 'Single Room'), ('Double', 'Double Room ')], max_length=15),
        ),
    ]
