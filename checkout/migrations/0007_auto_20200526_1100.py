# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-26 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_auto_20200526_1048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.AlterField(
            model_name='order',
            name='town_or_city',
            field=models.CharField(max_length=40),
        ),
    ]
