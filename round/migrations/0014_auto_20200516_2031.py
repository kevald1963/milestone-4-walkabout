# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-05-16 19:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('round', '0013_auto_20200516_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='street',
            name='round',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='round.Round'),
        ),
    ]