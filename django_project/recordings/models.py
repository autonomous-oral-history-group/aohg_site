# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.conf import settings
from audiofield.fields import AudioField
import os.path

# Add the audio field to your model
class Recording(models.Model):
	audio_file = AudioField(upload_to='recordings', blank=True,
                        ext_whitelist=(".mp3", ".wav", ".ogg"),
                        help_text=("Allowed type - .mp3, .wav, .ogg")) 

	def audio_file_player(self):
		 """audio player tag for admin"""
		 if self.audio_file:
			  file_url = settings.MEDIA_URL + str(self.audio_file)
			  player_string = '<audio src="%s" controls>Your browser does not support the audio element.</audio>' % (file_url)
			  return player_string

	audio_file_player.allow_tags = True
	audio_file_player.short_description = ('Audio file player')

