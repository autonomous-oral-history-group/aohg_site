# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-22 01:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recordings', '0004_auto_20190807_2219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recording',
            name='title',
        ),
    ]
