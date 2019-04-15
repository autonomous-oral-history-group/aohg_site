# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Page

# Register your models here.

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
	prepopulated_fields = { 'slug': ('title',)}
	fields = [ \
		'title', \
		'content', \
		'slug', \
	]

