# Generated by Django 4.0.6 on 2022-07-31 22:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_cart_options_alter_wishlist_options_and_more'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='wishlist',
        #     name='id',
        # ),
        # migrations.AddField(
        #     model_name='wishlist',
        #     name='user',
        #     field=models.OneToOneField(default=3, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        #     preserve_default=False,
        # ),
    ]
