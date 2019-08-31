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
	sidebar = models.ForeignKey(Sidebar, on_delete=models.PROTECT, blank=True, null=True, )

	def __str__(self):
		return self.title

	def __repr__(self):
		return self.title

class Request(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	full_name = models.CharField(\
		max_length=200, \
		blank = True, \
	)
	pronouns = models.CharField( \
		max_length=100, \
		blank=True, \
	)
	email = models.EmailField()
	items = models.ManyToManyField('names.Name')
	first_choice_date = models.DateField()
	first_choice_time = models.CharField( max_length=50, blank=True)
	second_choice_date = models.DateField()
	second_choice_time = models.CharField( max_length=50, blank=True)