# Generated by Django 3.2.12 on 2023-12-29 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='banner_area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='banner')),
                ('title', models.CharField(default='', max_length=100)),
                ('deal', models.CharField(default='', max_length=50)),
                ('sale', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('link', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
