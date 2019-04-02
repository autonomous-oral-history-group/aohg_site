# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Name

# Register your models here.

class NameAdmin(admin.ModelAdmin):
	pass

admin.site.register(Name, NameAdmin)
