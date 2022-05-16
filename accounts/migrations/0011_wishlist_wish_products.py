# Generated by Django 4.0.4 on 2022-05-16 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_previous_price'),
        ('accounts', '0010_remove_wishlist_wish_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='wish_products',
            field=models.ManyToManyField(blank=True, to='products.product'),
        ),
    ]
