# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-26 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('names', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(blank=True, max_length=120)),
                ('name', models.ManyToManyField(related_name='keywords', to='names.Name')),
            ],
        ),
    ]