# Generated by Django 3.2.12 on 2024-01-28 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_alter_blog_upload_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='upload_date',
            field=models.DateTimeField(),
        ),
    ]
