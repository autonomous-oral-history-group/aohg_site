# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Name
from sidebars.models import Sidebar


# Create your views here.

class NamesList(ListView):
	model = Name
	template_name = 'names/name_list.html'
	context_object_name = 'names'

	def get_sidebar_general_page(self):
		return Sidebar.objects.get(title='General')

	def get_context_data(self, **kwargs):
		context = super(NamesList, self).get_context_data(**kwargs) 
		context['sidebar'] = self.get_sidebar_general_page()
		return context



class NameDetail(DetailView):
	model = Name
	template_name = 'names/name_detail.html'
	context_object_name = 'name'
