# Generated by Django 4.0.4 on 2022-07-24 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0048_remove_game_id_remove_pc_id_remove_phone_id_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
