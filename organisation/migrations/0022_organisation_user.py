# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-25 19:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organisation', '0021_auto_20200425_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]