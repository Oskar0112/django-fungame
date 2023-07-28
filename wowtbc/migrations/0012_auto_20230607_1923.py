# Generated by Django 3.2.4 on 2023-06-07 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wowtbc', '0011_alter_cointypeimage_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='price',
            new_name='buy_price',
        ),
        migrations.AddField(
            model_name='game',
            name='sell_price',
            field=models.FloatField(default=1, help_text='Price per 1 Unit coins'),
            preserve_default=False,
        ),
    ]