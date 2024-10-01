# Generated by Django 5.0.4 on 2024-09-19 17:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0026_productsales'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_bookings', models.PositiveIntegerField(default=0)),
                ('total_deliveries', models.PositiveIntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grocery.product')),
            ],
        ),
        migrations.DeleteModel(
            name='ProductSales',
        ),
    ]
