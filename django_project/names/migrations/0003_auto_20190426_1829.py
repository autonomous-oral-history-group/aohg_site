# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-26 18:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('names', '0002_keyword'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='keyword',
            name='name',
        ),
        migrations.DeleteModel(
            name='Keyword',
        ),
    ]
