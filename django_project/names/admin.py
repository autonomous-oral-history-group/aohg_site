# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Name
from recordings.models import Recording

# Register your models here.


class RecordingInline(admin.TabularInline):
	model = Recording

class NameAdmin(admin.ModelAdmin):
	inlines = [ 
		RecordingInline,
	]

admin.site.register(Name, NameAdmin)
