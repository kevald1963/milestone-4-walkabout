# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-18 18:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_product_number_of_subscription_months'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='is_subscription_product',
            new_name='is_base_product',
        ),
    ]
