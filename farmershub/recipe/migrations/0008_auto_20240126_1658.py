# Generated by Django 3.2.12 on 2024-01-26 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0007_alter_recipe_cook_time_alter_recipe_prep_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]