# Generated by Django 4.0.6 on 2022-07-31 21:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customaccount_is_vendor'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='cart',
        #     name='id',
        # ),
        # migrations.RemoveField(
        #     model_name='wishlist',
        #     name='id',
        # ),
        # migrations.AlterField(
        #     model_name='cart',
        #     name='user',
        #     field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        # ),
        # migrations.AlterField(
        #     model_name='wishlist',
        #     name='user',
        #     field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        # ),
    ]
