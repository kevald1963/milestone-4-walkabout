# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-08 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200407_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_path',
            field=models.TextField(blank=True),
        ),
    ]
