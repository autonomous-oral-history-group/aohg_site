# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
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

	def get_context_data(self, **kwargs):
		context = super(PageDetail, self).get_context_data(**kwargs)
		context['menu'] = self.get_object().slug
		return context

class Index(TemplateView):
	model = Page
	template_name = 'pages/page_detail.html'
	context_object_name = 'page' 

	def get_context_data(self, **kwargs):
		context = super(Index, self).get_context_data(**kwargs)
		context['page'] = Page.objects.get(slug='about') 
		context['menu'] = 'about'
		return context


