# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-31 05:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bill_payment',
            fields=[
                ('id_bill_payment', models.IntegerField(primary_key=True, serialize=False)),
                ('payment_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='city',
            fields=[
                ('id_city', models.IntegerField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='client',
            fields=[
                ('name_client', models.CharField(max_length=20)),
                ('id_client', models.IntegerField(primary_key=True, serialize=False)),
                ('id_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coffeeshop.city')),
            ],
        ),
        migrations.CreateModel(
            name='departament',
            fields=[
                ('id_dpto', models.IntegerField(primary_key=True, serialize=False)),
                ('dpto_name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='description_bill_payment',
            fields=[
                ('id_payment', models.IntegerField(primary_key=True, serialize=False)),
                ('pay_mode', models.CharField(choices=[('CC', 'Credit Card'), ('CM', 'Cash Money')], default='CM', max_length=2)),
                ('employee_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id_product', models.IntegerField(primary_key=True, serialize=False)),
                ('name_product', models.CharField(max_length=20, unique=True)),
                ('price', models.DecimalField(decimal_places=7, max_digits=10)),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='product_type',
            fields=[
                ('id_product_type', models.IntegerField(primary_key=True, serialize=False)),
                ('product_type', models.CharField(max_length=30, unique=True)),
                ('product_description', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='provider',
            fields=[
                ('id_provider', models.IntegerField(primary_key=True, serialize=False)),
                ('provider_name', models.CharField(max_length=30)),
                ('tel_provider', models.IntegerField(unique=True)),
                ('id_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coffeeshop.city')),
            ],
        ),
        migrations.CreateModel(
            name='sale',
            fields=[
                ('id_sale', models.IntegerField(primary_key=True, serialize=False)),
                ('quantity_sold', models.IntegerField()),
                ('sale_value', models.DecimalField(decimal_places=7, max_digits=10)),
                ('id_bill_payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coffeeshop.bill_payment')),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coffeeshop.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='id_product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coffeeshop.product_type'),
        ),
        migrations.AddField(
            model_name='product',
            name='id_provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coffeeshop.provider'),
        ),
        migrations.AddField(
            model_name='city',
            name='id_dpto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coffeeshop.departament'),
        ),
        migrations.AddField(
            model_name='bill_payment',
            name='id_client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coffeeshop.client'),
        ),
        migrations.AddField(
            model_name='bill_payment',
            name='id_payment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coffeeshop.description_bill_payment'),
        ),
    ]
