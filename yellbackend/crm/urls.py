from django.conf.urls import url

from . import views

urlpatterns =[
	url(r'^$', views.course_show),
	url(r'^leads.html$', views.leads),
	url(r'^member.html$', views.member),
	url(r'^course_show.html$', views.course_show),
	url(r'^course_mgt.html$', views.course_mgt),	

]