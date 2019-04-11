# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Name


# Create your views here.

class NamesList(ListView):
	model = Name
	template_name = 'names/name_list.html'
	context_object_name = 'names'

class NameDetail(DetailView):
	model = Name
	template_name = 'names/name_detail.html'
	context_object_name = 'name'
