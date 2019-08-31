# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView
from django.forms.widgets import TextInput, EmailInput, DateInput, TimeInput
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

from .models import Page, Request


#from .forms import RequestForm
#from django.views.generic.edit import FormView

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


class RequestCreate(CreateView):
	model = Request
	fields = [ \
		'full_name', \
		'pronouns',\
		'email', \
		'items',\
		'first_choice_date',\
		'first_choice_time', \
		'second_choice_date', \
		'second_choice_time' \
	]
	widgets = {
		'pronouns': TextInput(attrs={\
			'placeholder':'e.g. they/them or she/her', \
			'autocomplete':'pronouns'\
		}),
		'full_name' : TextInput(
			attrs={
				'placeholder': 'Jane Doe'
			}
		)
	}
	success_url = '/request-success'
	success_message = "Your request has been received! We'll contact you shortly."

	def send_email(self, form):
		data = self.get_form_kwargs()['data']
		subject = "AOHG: Request from %s" % data['full_name']
		message = 'New request from %s' % data['full_name']
		message += "Email: %s \n" % data['email'] 
		message += "Pronouns: %s \n" % data['pronouns']
		message += "First choice date: %s \n" % data['first_choice_date']
		message += "First choice time: %s \n" % data['first_choice_time']
		message += "Second choice date: %s \n" % data['second_choice_date']
		message += "Second choice time: %s \n" % data['second_choice_time']
		from_email = form.fields['email']
		recipient_list = ['leilakari@mailinator.com']

		#print (subject, message, from_email, recipient_list)
		print(subject)
		print(message)
		#send_mail (subject, message, from_email, recipient_list, fail_silently=False)
		return True

	def get_context_data(self, **kwargs):
		context = super(RequestCreate, self).get_context_data(**kwargs)
		context['page'] = Page.objects.get(slug='request') 
		context['menu'] = 'request'
		#import pdb;pdb.set_trace()
		return context

	def form_valid(self, form):
		self.send_email(form)
		super(RequestCreate, self).form_valid(form)
		return HttpResponseRedirect(self.get_success_url())

 



"""
class RequestCreate(FormView):
    template_name = 'pages/page_detail.html'
    form_class = RequestForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(ContactView, self).form_valid(form)
"""