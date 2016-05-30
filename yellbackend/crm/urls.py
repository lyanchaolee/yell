from django.conf.urls import url

from . import views

app_name = 'crm'

urlpatterns =[
	url(r'^$', views.login),
	url(r'^$', views.course_show),
	url(r'^leads.html$', views.leads),
	url(r'^member.html$', views.member),
	url(r'^login.html$', views.login),
	url(r'^sign_out.html$', views.sign_out),
	url(r'^login_post.html$', views.login_post),
	url(r'^course_show.html$', views.course_show),
	url(r'^course_mgt.html$', views.course_mgt),	
	url(r'^test.html$', views.test),
	url(r'^lead_editing.html$', views.lead_editing),
	url(r'^reservation.html$', views.reservation),
	url(r'^resrvation_post.html$', views.resrvation_post),
	url(r'^appoints.html$', views.appoints),
	url(r'^appoints_post.html$', views.appoints_post),
	url(r'^remark.html$', views.remark),
	url(r'^remark_post.html$', views.remark_post),
	url(r'^leads_filter.html$', views.leads_filter),
	url(r'^leads_upload.html$', views.leads_upload),
	url(r'^payment.html$', views.payment),
	url(r'^payment_post.html$', views.payment_post),	

]