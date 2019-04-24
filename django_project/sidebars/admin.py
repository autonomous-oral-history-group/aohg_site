# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Sidebar

# Register your models here.

@admin.register(Sidebar)
class SidebarAdmin(admin.ModelAdmin):
	fields = [ \
		'title', \
		'content', \
	]


