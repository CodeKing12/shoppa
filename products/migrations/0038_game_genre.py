# Generated by Django 4.0.4 on 2022-07-23 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0037_remove_game_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='genre',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.gamegenres'),
            preserve_default=False,
        ),
    ]
