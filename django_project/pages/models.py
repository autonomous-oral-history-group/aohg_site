# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField 
from sidebars.models import Sidebar

# Create your models here.

class Page(models.Model):
	title = models.CharField(max_length=120) 
	slug = models.SlugField( \
		unique=True, \
		blank=True, \
		null=True,
	) 
	content = HTMLField(blank=True) 
	sidebar = models.ForeignKey(Sidebar, on_delete=models.PROTECT, blank=True, null=True)

	def __str__(self):
		return self.title
	
	def __repr__(self):
		return self.title

