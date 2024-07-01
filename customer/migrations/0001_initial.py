# Generated by Django 5.0.6 on 2024-06-30 18:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=155, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=150, null=True)),
                ('joined', models.DateTimeField(default=datetime.datetime(2024, 6, 30, 23, 39, 48, 757657))),
                ('image', models.ImageField(blank=True, null=True, upload_to='customer/')),
            ],
            options={
                'verbose_name_plural': 'Customers',
                'ordering': ('-joined',),
            },
        ),
    ]