# Generated by Django 3.2.12 on 2024-01-13 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_auto_20240112_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_featured',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
