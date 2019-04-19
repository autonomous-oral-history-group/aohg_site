# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Page


# Create your views here.

"""
class PageList(ListView):
	model = Name
	template_name = 'pages/page_list.html'
	context_object_name = 'page'
"""

class PageDetail(DetailView):
	model = Page
	template_name = 'pages/page_detail.html'
	context_object_name = 'page' 
