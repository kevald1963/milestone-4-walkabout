# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-19 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0012_auto_20200310_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='home_number',
            field=models.CharField(blank=True, max_length=14),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=14),
        ),
    ]
