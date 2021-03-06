# Generated by Django 4.0.6 on 2022-07-28 04:52

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VendorAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_first_name', models.CharField(max_length=100)),
                ('owner_middle_name', models.CharField(max_length=100)),
                ('owner_last_name', models.CharField(max_length=100)),
                ('owner_dob', models.DateTimeField()),
                ('owner_id', models.ImageField(upload_to='vendors_id')),
                ('owner_image', models.ImageField(upload_to='vendors_images')),
                ('cac_reg_num', models.IntegerField()),
                ('tax_id_num', models.IntegerField(blank=True)),
                ('nin', models.IntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(blank=True, max_length=70, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('business_name', models.CharField(max_length=150, unique=True)),
                ('address', models.CharField(max_length=200)),
                ('business_description', models.TextField(max_length=160)),
                ('twitter_link', models.URLField(blank=True)),
                ('facebook_link', models.URLField(blank=True)),
                ('whatsapp_link', models.URLField(blank=True)),
                ('instagram_link', models.URLField(blank=True)),
                ('company_start_date', models.DateTimeField()),
                ('amount_made', models.IntegerField()),
                ('orders_completed', models.IntegerField()),
                ('products_in_stock', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VendorReviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(5)])),
                ('review', models.TextField(max_length=200)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendors.vendoraccount')),
            ],
        ),
        migrations.CreateModel(
            name='VendorMessages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('message', models.TextField(max_length=200)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendors.vendoraccount')),
            ],
        ),
    ]
