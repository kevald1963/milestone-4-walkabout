# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-18 16:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0016_auto_20200417_2144'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscription',
            options={'ordering': ['organisation', 'product']},
        ),
        migrations.RenameField(
            model_name='subscription',
            old_name='product_number',
            new_name='product',
        ),
    ]