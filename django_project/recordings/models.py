# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from wagtailmedia.edit_handlers import MediaChooserPanel


# Create your models here.

from django.conf import settings
import os.path

# Add the audio field to your model
class Recording(models.Model):
	audio_file = models.ForeignKey(
        'wagtailmedia.Media',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    ) 
