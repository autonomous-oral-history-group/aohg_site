# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField 
from django.utils.text import slugify
import tagulous.models
from datetime import date 

# Create your models here.

class Name(models.Model):
	name = models.CharField(max_length=120)
	call_number = models.CharField(max_length=120, blank=True) 
	location = models.CharField(max_length=120, blank=True) 
	summary = HTMLField(blank=True) 
	date_published = models.DateField(blank=True, default=date.today)
	city_published = models.CharField(blank=True, default='Los Angeles', verbose_name='City Published', max_length=80)
	archivist_summary = HTMLField(blank=True) 
	archivist_ethics = HTMLField(blank=True) 
	access_conditions = models.CharField(max_length=160,blank=True)
	created_published_by = models.CharField(max_length=160,blank=True, verbose_name = 'Created / Published By')
	bio_hist_note = HTMLField("Bio./Hist. Note", blank=True) 
	slug = models.SlugField( \
		unique=True, \
		blank=True, \
		null=True, \
		max_length=160,
	) 
	#subjects = tagulous.models.TagField(related_name="subject")
	subjects = models.ManyToManyField('Subject', related_name="subject", blank=True)

	@property
	def recordings(self):
		return self.recording_set.all()

	@property
	def num_recordings(self):
			return self.recording_set.count()

	def save(self, *args, **kwargs):
		# If there isn't a slug, make it
		if (self.slug is None):
			self.slug = slugify(self.name)
		super(Name, self).save(*args, **kwargs)

	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.name
	
class Subject (tagulous.models.TagModel):
	
	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.name

