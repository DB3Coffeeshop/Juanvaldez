# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-15 04:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coffeeshop', '0004_auto_20170514_1708'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='points',
        ),
    ]