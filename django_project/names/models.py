# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Name(model.Models):
	name = models.CharField(max_length=120, primary_key=True)