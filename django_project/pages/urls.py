from django.conf.urls import url 
from .views import PageDetail

urlpatterns=[
	url(r'^(?P<slug>[\w-]+)$', PageDetail.as_view(), name='page_detail'), 
]

