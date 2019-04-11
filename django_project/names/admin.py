# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Name
from recordings.models import Recording
from django.utils.text import slugify

# Register your models here.


class RecordingInline(admin.TabularInline):
	model = Recording

class NameAdmin(admin.ModelAdmin):
	prepopulated_fields = { 'slug': ('name',)}
	fields = [ \
		'name', 'description', 'slug' \
	]
	list_display = [ \
		'name',  \
	]
	inlines = [ 
		RecordingInline,
	]

admin.site.register(Name, NameAdmin)
