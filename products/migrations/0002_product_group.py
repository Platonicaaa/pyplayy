# Generated by Django 3.2.4 on 2021-07-23 08:17

import django.db.models.deletion
from django.db import migrations, models


def create_default_groups(apps, _):
    ProductGroup = apps.get_model('products', 'ProductGroup')
    Product = apps.get_model('products', 'Product')

    fruits, _ = ProductGroup.objects.get_or_create(name='Fruits')
    vegetables, _ = ProductGroup.objects.get_or_create(name='Vegetables')

    for product in Product.objects.all():
        if product.category == 'FRU':
            product.product_group_id = fruits
        else:
            product.product_group_id = vegetables
        product.save()


def rollback_product_groups(apps, _):
    ProductGroup = apps.get_model('products', 'ProductGroup')
    Product = apps.get_model('products', 'Product')

    fruits = ProductGroup.objects.get(name='Fruits')

    for product in Product.objects.all():
        if product.product_group_id == fruits:
            product.category = 'FRU'
        else:
            product.category = 'VEG'
        product.save()


class Migration(migrations.Migration):
    dependencies = [
        ('products', '0001_initial'),
    ]
    operations = [
        migrations.CreateModel(
            name='ProductGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('FRU', 'Fruits'), ('VEG', 'Vegetables')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_group_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.productgroup'),
        ),
        migrations.RunPython(create_default_groups, rollback_product_groups),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AlterField(
            model_name='product',
            name='product_group_id',
            field=models.ForeignKey(null=False, on_delete=django.db.models.deletion.CASCADE, to='products.productgroup'),
        ),
    ]
