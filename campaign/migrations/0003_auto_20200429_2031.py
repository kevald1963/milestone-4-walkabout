# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-29 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0002_auto_20200429_2013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campaign',
            old_name='contact_name',
            new_name='campaign_lead',
        ),
        migrations.AlterField(
            model_name='campaign',
            name='campaign_type',
            field=models.CharField(choices=[('LE', 'Leafleting'), ('CA', 'Canvassing'), ('SU', 'Surveying')], default='LE', max_length=15),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='end_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='start_date',
            field=models.DateField(),
        ),
    ]
