# Generated by Django 3.2.12 on 2023-12-30 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20231230_0538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner_area',
            name='category',
        ),
        migrations.AddField(
            model_name='banner_area',
            name='deal',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='banner_area',
            name='link',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='banner_area',
            name='sale',
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('Currentprice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Oldprice', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('image', models.ImageField(null=True, upload_to='newproducts')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.categories')),
            ],
        ),
    ]
