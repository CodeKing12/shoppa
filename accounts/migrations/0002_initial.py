# Generated by Django 4.0.6 on 2022-07-28 04:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='wish_products',
            field=models.ManyToManyField(blank=True, to='products.product'),
        ),
        migrations.AddField(
            model_name='cartdetails',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.cart'),
        ),
        migrations.AddField(
            model_name='cartdetails',
            name='product',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
        migrations.AddField(
            model_name='cart',
            name='cart_products',
            field=models.ManyToManyField(blank=True, through='accounts.CartDetails', to='products.product'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='apiuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='customaccount',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='customaccount',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]