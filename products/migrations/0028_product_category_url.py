# Generated by Django 4.0.4 on 2022-07-20 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_product_content_type_product_object_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category_url',
            field=models.CharField(default='laptops', max_length=100),
            preserve_default=False,
        ),
    ]
