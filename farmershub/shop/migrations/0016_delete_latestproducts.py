# Generated by Django 5.0 on 2024-01-13 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_product_is_featured'),
    ]

    operations = [
        migrations.DeleteModel(
            name='latestProducts',
        ),
    ]
