# Generated by Django 3.1.4 on 2021-01-28 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0013_auto_20210128_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='category',
            field=models.CharField(choices=[('Triple', 'Triple Room'), ('Non-Conditioned', 'Non-Conditioned'), ('Deluxe', 'Deluxe Rooom'), ('Single', 'Single Room'), ('Double', 'Double Room ')], max_length=15),
        ),
    ]