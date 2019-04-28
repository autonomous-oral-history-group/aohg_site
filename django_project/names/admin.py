# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Name, Keyword
#from .models import Name
from recordings.models import Recording

from django.utils.text import slugify
#import tagulous 
import tagulous.admin 
from . import models

# Register your models here.


class RecordingInline(admin.StackedInline): 
	prepopulated_fields = { 'slug': ('title',)}
	model = Recording
	extra = 0

class KeywordInline(admin.StackedInline):
	model = Keyword
	extra = 0

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
		'keywords'
	]

	list_display = [ \
		'name',  \
	]

	inlines = [ 
		RecordingInline,
		#KeywordInline,
	]

#import pdb; pdb.set_trace()
#tagulous.admin.register(Name, NameAdmin)
#tag_enhance(Keyword, KeywordInline)
#tag_enhance(Keyword, KeywordAdmin)
#tag_enhance(Name, NameAdmin)
tagulous.admin.register(models.Name)
tagulous.admin.register(models.Keyword)
#admin.site.register(Keyword, KeywordAdmin)
