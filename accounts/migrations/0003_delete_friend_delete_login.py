# Generated by Django 4.0.4 on 2022-05-10 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_cart_friend_login_wishlist_cartdetails_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Friend',
        ),
        migrations.DeleteModel(
            name='Login',
        ),
    ]