# Generated by Django 4.0.4 on 2022-07-22 22:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0033_gamegenres'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameGenres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='productreviews',
            name='review_title',
            field=models.CharField(default='This is a demo review title', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productreviews',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='genre',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.gamegenres'),
            preserve_default=False,
        ),
    ]
