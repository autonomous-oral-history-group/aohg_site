# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Name, Subject
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

class SubjectInline(admin.StackedInline):
	model = Subject
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
		'subjects'
	]

	list_display = [ \
		'name',  \
	]

	inlines = [ 
		RecordingInline,
		#SubjectInline,
	]

#import pdb; pdb.set_trace()
#tagulous.admin.register(Name, NameAdmin)
#tag_enhance(Subject, SubjectInline)
#tag_enhance(Subject, SubjectAdmin)
#tag_enhance(Name, NameAdmin)
tagulous.admin.register(models.Name)
tagulous.admin.register(models.Subject)
#admin.site.register(Subject, SubjectAdmin)
