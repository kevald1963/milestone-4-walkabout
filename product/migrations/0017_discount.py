# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-21 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_auto_20200418_1957'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.SmallIntegerField(unique=True)),
                ('type', models.CharField(default='', max_length=40)),
                ('percent', models.SmallIntegerField()),
            ],
            options={
                'ordering': ['code', 'type'],
            },
        ),
    ]
