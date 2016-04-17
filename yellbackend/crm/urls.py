from django.conf.urls import url

from . import views

app_name = 'crm'

urlpatterns =[
	url(r'^$', views.login),
	url(r'^$', views.course_show),
	url(r'^leads.html$', views.leads),
	url(r'^member.html$', views.member),
	url(r'^login.html$', views.login),
	url(r'^login_post.html$', views.login_post),
	url(r'^register.html$', views.register),
	url(r'^register_post.html$', views.register_post),
	url(r'^course_show.html$', views.course_show),
	url(r'^course_mgt.html$', views.course_mgt),	

]