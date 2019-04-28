from django.conf.urls import url 
from .views import NamesList, NameDetail, SubjectList, SubjectDetail

urlpatterns=[
	url(r'^name(/)?$', NamesList.as_view(), name='names_list'), 
	url(r'^name/(?P<slug>[\w-]+)$', NameDetail.as_view(), name='name_detail'), 
	url(r'^subject$', SubjectList.as_view(), name='subject_list'), 
	url(r'^subject/(?P<slug>[\w-]+)$', SubjectDetail.as_view(), name='subject_detail'), 
]
