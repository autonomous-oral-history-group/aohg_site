# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-22 01:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('names', '0011_auto_20190822_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='name',
            name='city_published',
            field=models.TextField(blank=True, default='Los Angeles', verbose_name='City Published'),
        ),
    ]
