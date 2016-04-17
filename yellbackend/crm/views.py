from django.http import HttpResponse
from django.template import loader
from .models import Customer
from .models import Remark

def course_mgt(request):
	customer_list=Customer.objects.order_by('-id')[:5]
	template=loader.get_template('crm/course_mgt.html')
	context={
		'customer_list':customer_list
	}
	
	return HttpResponse(template.render(context, request))
	
def leads(request):
	customer_list=Customer.objects.order_by('id')[:5]
	
	for customer in customer_list:
		all_remark=Remark.objects.filter(refer_id=customer.id, refer_type='Leads').order_by('id')
		if all_remark.count() > 0:
			first_remark=all_remark[0]
			customer.remark_list=all_remark[1:]
			customer.remark_size=all_remark.count()
			customer.first_remark=first_remark
		else:
			first_remark=Remark()
			first_remark.remark=""
			customer.first_remark=""
		
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
	
		
