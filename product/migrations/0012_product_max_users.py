# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-17 16:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_product_max_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='max_users',
            field=models.SmallIntegerField(default=0),
        ),
    ]
