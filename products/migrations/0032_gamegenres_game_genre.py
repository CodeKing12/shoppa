# Generated by Django 4.0.4 on 2022-07-22 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0031_delete_gamegenres'),
    ]

    operations = [
        # migrations.CreateModel(
        #     name='GameGenres',
        #     fields=[
        #         ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('name', models.CharField(max_length=150)),
        #     ],
        # ),
        # migrations.AddField(
        #     model_name='game',
        #     name='genre',
        #     field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.gamegenres'),
        #     preserve_default=False,
        # ),
    ]
