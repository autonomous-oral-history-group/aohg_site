# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField 

# Create your models here.

class Name(models.Model):
	name = models.CharField(max_length=120, primary_key=True)
	description = HTMLField() 
