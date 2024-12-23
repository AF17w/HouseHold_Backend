# Generated by Django 4.2.15 on 2024-09-03 18:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SellerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('account_type', models.CharField(default='seller_account', max_length=20)),
                ('service_category', models.CharField(choices=[('electrician', 'Electrician'), ('plumber', 'Plumber'), ('internet', 'Internet Fixer'), ('cleaner', 'House Cleaner')], max_length=50)),
                ('completed_jobs', models.IntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BuyerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('account_type', models.CharField(default='buyer_account', max_length=50)),
                ('total_bought', models.IntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='buyer_profile')),
            ],
        ),
    ]
