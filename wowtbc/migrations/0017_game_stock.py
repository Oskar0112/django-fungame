# Generated by Django 3.2.4 on 2023-06-17 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wowtbc', '0016_game_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='stock',
            field=models.CharField(default='0M', help_text='e.g 100K or 100M', max_length=10),
        ),
    ]
