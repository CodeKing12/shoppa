# Generated by Django 4.0.4 on 2022-07-23 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0040_alter_product_object_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]
