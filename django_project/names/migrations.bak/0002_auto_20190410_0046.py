# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-10 00:46
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('names', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='name',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]
