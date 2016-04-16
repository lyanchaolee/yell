from django.http import HttpResponse
from django.template import loader
from .models import Customer

def course_mgt(request):
	customer_list=Customer.objects
	template=loader.get_template('crm/course_mgt.html')
	context={
		'customer_list':customer_list
	}
	
	return HttpResponse(template.render(context, request))
	
def leads(request):
	customer_list=Customer.objects
	template=loader.get_template('crm/leads.html')
	context={
		'customer_list':customer_list
	}
	
	return HttpResponse(template.render(context, request))


def member(request):
	customer_list=Customer.objects
	template=loader.get_template('crm/member.html')
	context={
		'customer_list':customer_list
	}
	
	return HttpResponse(template.render(context, request))
	
def course_show(request):
	customer_list=Customer.objects
	template=loader.get_template('crm/course_show.html')
	context={
		'customer_list':customer_list
	}
	
	return HttpResponse(template.render(context, request))
	
		
