# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-22 00:21
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('names', '0008_auto_20190821_2320'),
    ]

    operations = [
        migrations.AddField(
            model_name='name',
            name='archivist_ethics',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]
