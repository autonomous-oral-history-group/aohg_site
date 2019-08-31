from django.conf.urls import url 
from .views import PageDetail, RequestCreate

urlpatterns=[
	url(r'^request$', RequestCreate.as_view(), name='request-form'), 
	url(r'^(?P<slug>[\w-]+)$', PageDetail.as_view(), name='page_detail'), 
]

