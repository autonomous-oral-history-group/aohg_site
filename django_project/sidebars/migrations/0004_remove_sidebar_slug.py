# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-24 19:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sidebars', '0003_remove_sidebar_page'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sidebar',
            name='slug',
        ),
    ]