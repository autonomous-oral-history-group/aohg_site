# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField 

# Create your models here.

class Sidebar(models.Model):
	title = models.CharField(max_length=120) 
	content = HTMLField(blank=True) 

	def __str__(self):
		return self.title
	
	def __repr__(self):
		return self.title


