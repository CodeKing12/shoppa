# Generated by Django 4.0.4 on 2022-05-16 12:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_customaccount_address_delete_addressbook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customaccount',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.DeleteModel(
            name='PhoneBook',
        ),
    ]
