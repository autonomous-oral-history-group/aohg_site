# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-31 00:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20190830_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]