# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-12 02:30
from __future__ import unicode_literals

import audiofield.fields
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('names', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recording',
            fields=[
                ('title', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('transcript', tinymce.models.HTMLField(blank=True)),
                ('audio_file', audiofield.fields.AudioField(blank=True, help_text='Allowed type - .mp3, .wav, .ogg', upload_to='recordings')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('names', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='names.Name')),
            ],
        ),
    ]
