# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-14 18:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coffeeshop', '0002_auto_20170511_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id_product_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coffeeshop.Product_type'),
        ),
    ]
