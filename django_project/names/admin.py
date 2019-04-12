# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Name
from recordings.models import Recording
from django.utils.text import slugify

# Register your models here.


class RecordingInline(admin.StackedInline): 
	prepopulated_fields = { 'slug': ('title',)}
	model = Recording
	extra = 1

@admin.register(Name)
class NameAdmin(admin.ModelAdmin):
	prepopulated_fields = { 'slug': ('name',)}
	fields = [ \
		'name', \
		'slug', \
		'call_number', \
		'location', \
		'summary', \
		'archivist_summary', \
		'access_conditions', \
		'created_published_by', \
		'extent', \
	]

	list_display = [ \
		'name',  \
	]

	inlines = [ 
		RecordingInline,
	]

#admin.site.register(Name, NameAdmin)
