# Generated by Django 4.0.6 on 2022-07-31 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_remove_wishlist_id_wishlist_user'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='cartdetails',
        #     name='cart',
        # ),
        # migrations.RemoveField(
        #     model_name='cartdetails',
        #     name='product',
        # ),
        # migrations.RemoveField(
        #     model_name='wishlist',
        #     name='user',
        # ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartDetails',
        ),
        migrations.DeleteModel(
            name='Wishlist',
        ),
    ]
