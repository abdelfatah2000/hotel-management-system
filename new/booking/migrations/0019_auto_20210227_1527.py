# Generated by Django 3.1.4 on 2021-02-27 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0018_auto_20210202_2308'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'verbose_name': 'Room', 'verbose_name_plural': 'Rooms'},
        ),
        migrations.AlterField(
            model_name='room',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
