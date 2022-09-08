# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

from django.db import models
from tinymce.models import HTMLField 
from sidebars.models import Sidebar 
from django.core.mail import send_mail

# Create your models here.

class Page(models.Model):
	title = models.CharField(max_length=120) 
	slug = models.SlugField( \
		unique=True, \
		blank=True, \
		null=True,
	) 
	content = HTMLField(blank=True) 
	sidebar = models.ForeignKey(Sidebar, on_delete=models.PROTECT, blank=True, null=True, )

	def __str__(self):
		return self.title

	def __repr__(self):
		return self.title

class Request(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	full_name = models.CharField(\
		max_length=200, \
		blank = True, \
	)
	pronouns = models.CharField( \
		max_length=100, \
		blank=True, \
	)
	email = models.EmailField()
	items = models.ManyToManyField('names.Name')
	first_choice_date = models.DateField()
	first_choice_time = models.CharField( max_length=50, blank=True)
	second_choice_date = models.DateField()
	second_choice_time = models.CharField( max_length=50, blank=True) 

	def get_email_to(self):
		try:
			return os.environ['EMAIL_TO']
		except:
			raise ImproperlyConfigured('EMAIL_TO')
			return 'info@aohistorygroup.com'

	def get_email_subject(self): 
		return("New request from: %s - Oral History Center" % self.full_name)

	def get_item_list_string(self):
		r = ''
		for i in self.items.all():
			r += '\n - '
			r += i
		return r 

	def get_email_body(self): 
		body = "A new request has been logged through the Oral History Center site (aohistorygroup.com)."
		body += "\n\n"
		body += "Email: %s" % self.email
		body += "\n"
		body += "Name: %s" % self.full_name
		body += "\n"
		body += "Preferred gender pronouns: %s" % self.pronouns
		body += "\n"
		body += "Items they want to see: %s" % self.get_item_list_string()
		body += "\n"
		body += "First Choice: %s @ %s" % (self.first_choice_date, self.first_choice_time)
		body += "\n"
		body += "Second Choice: %s @ %s" % (self.second_choice_date, self.second_choice_time )
		body += "\n"
		return body

	def send_request_email(self, email): 
		# https://docs.djangoproject.com/en/1.11/topics/email/
		send_mail(
			self.get_email_subject(), 
			self.get_email_body(),
			'do_not_reply@aohistorygroup.com',
			[email],
			fail_silently=False,
		)

	def save(self, *args, **kwargs): 
		super(Request, self).save(*args, **kwargs)
		#self.send_request_email( self.get_email_to() ) 
	

