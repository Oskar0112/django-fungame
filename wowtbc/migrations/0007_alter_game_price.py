# Generated by Django 3.2 on 2023-05-31 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wowtbc', '0006_auto_20230530_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='price',
            field=models.FloatField(help_text='Price per 1M coins'),
        ),
    ]
