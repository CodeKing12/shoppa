# Generated by Django 4.0.4 on 2022-07-23 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('products', '0035_rename_user_productreviews_reviewer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pc',
            name='manufacturer',
            field=models.CharField(choices=[('AORUS', 'AORUS'), ('HP', 'HP'), ('LENOVO', 'LENOVO'), ('MSI', 'MSI'), ('ASUS', 'ASUS'), ('DELL', 'DELL'), ('ACER', 'ACER'), ('GIGABYTE', 'GIGABYTE'), ('MICROSOFT', 'MICROSOFT'), ('ALIENWARE', 'ALIENWARE'), ('APPLE', 'APPLE'), ('RAZER', 'RAZER'), ('SAMSUNG', 'SAMSUNG'), ('LG', 'LG'), ('TOSHIBA', 'TOSHIBA'), ('FUJITSU', 'FUJITSU'), ('PANASONIC', 'PANASONIC'), ('HUAWEI', 'HUAWEI'), ('DYNABOOK', 'DYNABOOK'), ('LAPTOPMEDIA', 'LAPTOPMEDIA'), ('INFINIX', 'INFINIX'), ('XIAOMI', 'XIAOMI'), ('SONY', 'SONY'), ('TOSHIBA', 'TOSHIBA'), ('DURABOOK', 'DURABOOK'), ('GOOGLE', 'GOOGLE'), ('NOKIA', 'NOKIA'), ('VAIO', 'VAIO'), ('PACKARD BELL', 'PACKARD BELL'), ('MSi', 'MSi'), ('HYUNDAI TECHNOLOGY', 'HYUNDAI TECHNOLOGY'), ('PREDATOR', 'PREDATOR')], default='SAMSUNG', max_length=60),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('PHONE', 'PHONE'), ('PC', 'LAPTOP'), ('REFURBISHED', 'REFURBISHED PRODUCT'), ('ACCESSORY', 'TECH ACCESSORY'), ('APPLIANCE', 'OFFICE APPLIANCE'), ('GAME', 'VIDEO GAME')], default='PC', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='content_type',
            field=models.ForeignKey(default=8, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
    ]
