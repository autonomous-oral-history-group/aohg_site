# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Page
from sidebars.models import Sidebar 

# Register your models here.

class SidebarInlineAdmin(admin.TabularInline):
	model = Sidebar
	fields = [ \
		'title',\
		'content',\
	]


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
	prepopulated_fields = { 'slug': ('title',)}
	fields = [ \
		'title', \
		'content', \
		'slug', \
		'sidebar',\
	]
	#inlines = [SidebarInlineAdmin]


