# Generated by Django 3.2.12 on 2023-12-29 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20231229_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner_area',
            name='link',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='categories',
            name='title',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
