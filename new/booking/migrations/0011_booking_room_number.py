# Generated by Django 3.1.4 on 2021-01-14 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0010_auto_20210114_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='room_number',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
