# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-20 19:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0016_auto_20200418_1957'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Enter name of your organisation or your full '
                                                                      'name if not an organisation.')),
                ('contact_name', models.CharField(max_length=50)),
                ('address_1', models.CharField(max_length=40)),
                ('address_2', models.CharField(max_length=40)),
                ('address_3', models.CharField(blank=True, max_length=40)),
                ('address_4', models.CharField(blank=True, max_length=40)),
                ('post_code', models.CharField(max_length=10)),
                ('email_address', models.EmailField(max_length=40)),
                ('landline_number', models.CharField(blank=True, max_length=14)),
                ('mobile_number', models.CharField(blank=True, max_length=14)),
                ('date', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkout.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
            ],
        ),
    ]
