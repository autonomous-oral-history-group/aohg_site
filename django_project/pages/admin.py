# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Page, Request
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
	list_display = ('title', 'slug')


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
	fields = [ \
		'full_name', \
		'pronouns',\
		'email', \
		'items',\
		'first_choice_date',\
		'first_choice_time', \
		'second_choice_date', \
		'second_choice_time' \
	]
	list_display = ('full_name','email','pronouns','created_at','first_choice_date','first_choice_time', 'second_choice_date', 'second_choice_time')

