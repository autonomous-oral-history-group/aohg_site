from django.conf.urls import url 
from .views import NamesList, NameDetail

urlpatterns=[
	url(r'^$', NamesList.as_view()), 
	url(r'^(?P<slug>[\w-]+)$', NameDetail.as_view()), 
]
