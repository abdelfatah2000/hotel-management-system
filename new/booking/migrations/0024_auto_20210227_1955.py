# Generated by Django 3.1.4 on 2021-02-27 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0023_auto_20210227_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='category',
            field=models.CharField(choices=[('Triple', 'Triple Room'), ('Non-Conditioned 2', 'Non-Conditioned'), ('Non-Conditioned 3', 'Non-Conditioned '), ('Deluxe', 'Deluxe Rooom'), ('Single', 'Single Room'), ('Double', 'Double Room ')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]
