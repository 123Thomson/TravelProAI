# Generated by Django 5.0.4 on 2024-09-19 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0024_delete_sales_booking_product_cart_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
