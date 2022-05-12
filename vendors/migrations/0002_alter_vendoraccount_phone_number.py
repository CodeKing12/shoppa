# Generated by Django 4.0.4 on 2022-05-12 00:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendoraccount',
            name='phone_number',
            field=models.CharField(blank=True, default='+234094854', max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
            preserve_default=False,
        ),
    ]