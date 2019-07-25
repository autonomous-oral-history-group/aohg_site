# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Name, Subject
from sidebars.models import Sidebar
from django.db.models.functions import Lower


# Create your views here.

class NamesList(ListView):
	model = Name
	template_name = 'names/name_list.html'
	context_object_name = 'names'
	paginate_by = 200

	def get_sidebar_general_page(self):
		return Sidebar.objects.get(title='General')

	def get_context_data(self, **kwargs):
		context = super(NamesList, self).get_context_data(**kwargs) 
		context['names'] = Name.objects.all().annotate(name_lower=Lower('name')).order_by('name_lower')
		context['sidebar'] = self.get_sidebar_general_page()
		context['menu'] = 'names'
		return context 

class NameDetail(DetailView):
	model = Name
	template_name = 'names/name_detail.html'
	context_object_name = 'name'

	def get_context_data(self, **kwargs):
		context = super(NameDetail, self).get_context_data(**kwargs)
		context['menu'] = 'names'
		return context


class SubjectList(ListView):
	model = Subject
	template_name = 'subjects/subject_list.html'
	context_object_name = 'subjects' 
	paginate_by = 200

	def get_context_data(self, **kwargs):
		context = super(SubjectList, self).get_context_data(**kwargs)
		context['subjects'] = Subject.objects.all().annotate(name_lower=Lower('name')).order_by('name_lower')
		context['menu'] = 'subjects'
		return context

class SubjectDetail(DetailView):
	model = Subject
	template_name = 'subjects/subject_detail.html'
	context_object_name = 'subject' 

	def get_context_data(self, **kwargs):
		context = super(SubjectDetail, self).get_context_data(**kwargs) 
		filter_slug = self.object.slug
		context['names'] = Name.objects.filter(subjects__slug=filter_slug )
		context['menu'] = 'subjects'
		return context

