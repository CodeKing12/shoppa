# Generated by Django 4.0.4 on 2022-07-15 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_alter_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_type',
            new_name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(auto_created=True, blank=True),
        ),
    ]
