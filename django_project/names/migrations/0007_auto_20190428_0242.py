# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-28 02:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('names', '0006_auto_20190426_2058'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Keyword',
            new_name='Subject',
        ),
        migrations.RemoveField(
            model_name='name',
            name='keywords',
        ),
        migrations.AddField(
            model_name='name',
            name='subjects',
            field=models.ManyToManyField(blank=True, related_name='subject', to='names.Subject'),
        ),
    ]
