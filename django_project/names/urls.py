from django.conf.urls import url 
from .views import NamesList, NameDetail, KeywordList, KeywordDetail

urlpatterns=[
	url(r'^name$', NamesList.as_view(), name='names_list'), 
	url(r'^name/(?P<slug>[\w-]+)$', NameDetail.as_view(), name='name_detail'), 
	url(r'^keyword$', KeywordList.as_view(), name='keyword_list'), 
	url(r'^keyword/(?P<slug>[\w-]+)$', KeywordDetail.as_view(), name='keyword_detail'), 
]
