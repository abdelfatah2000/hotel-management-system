# Generated by Django 3.1.4 on 2021-02-28 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0026_auto_20210228_0214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
            ],
        ),
    ]