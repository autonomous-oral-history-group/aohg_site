# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Name, Subject
from sidebars.models import Sidebar


# Create your views here.

class NamesList(ListView):
	model = Name
	template_name = 'names/name_list.html'
	context_object_name = 'names'
	ordering = 'name'
	paginate_by = 100

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


class SubjectList(ListView):
	model = Subject
	template_name = 'subjects/subject_list.html'
	context_object_name = 'subjects' 
	ordering = 'name'

class SubjectDetail(DetailView):
	model = Subject
	template_name = 'subjects/subject_detail.html'
	context_object_name = 'subject' 

	def get_context_data(self, **kwargs):
		context = super(SubjectDetail, self).get_context_data(**kwargs) 
		filter_slug = self.object.slug
		context['names'] = Name.objects.filter(subjects__slug=filter_slug )
		return context

