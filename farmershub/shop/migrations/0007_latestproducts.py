# Generated by Django 3.2.12 on 2023-12-30 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_remove_categories_discount'),
    ]

    operations = [
        migrations.CreateModel(
            name='latestProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('Currentprice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Oldprice', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('Discount', models.IntegerField()),
                ('image', models.ImageField(null=True, upload_to='newproducts')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.categories')),
            ],
        ),
    ]