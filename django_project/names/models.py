# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField 
from django.utils.text import slugify

# Create your models here.

class Name(models.Model):
	name = models.CharField(max_length=120, primary_key=True)
	description = HTMLField() 
	slug = models.SlugField( \
		unique=True, \
		blank=True, \
		null=True,
	) 

	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.name
	
	def save(self, *args, **kwargs):
		#if len(self.slug <= 0):
			#self.slug = slugify(name)
		super(Name, self).save(*args, **kwargs)
		
