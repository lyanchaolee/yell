from django.http import HttpResponse
from django.template import loader,RequestContext
from .models import Customer
from .models import Remark
from .models import Sales
from django.contrib.auth.hashers import make_password,check_password

def course_mgt(request):
	customer_list=Customer.objects.order_by('-id')[:5]
	template=loader.get_template('crm/course_mgt.html')
	context={
		'customer_list':customer_list
	}
	
	return HttpResponse(template.render(context, request))
	

def login(request):

	template=loader.get_template('crm/login.html')
	
	return HttpResponse(template.render(RequestContext(request)))

def login_post(request):
	sales=Sales.objects.get(username=request.POST.get('username'))
	passinput=request.POST.get('password')
	if check_password(passinput,sales.password):
		template=loader.get_template('crm/leads.html')
		response=HttpResponse(template.render(RequestContext(request)))
		response.set_cookie("is_login","True")
		response.set_cookie("user_id",sales.id)
		return response
	else:
		return HttpResponse("LOGIN FAIL"+sales.password+passinput)
		
def get_leads(sales_identify):

	customer_list=Customer.objects.filer(sales_id=sales_identify).order_by('-id')
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
	return context
		
def register_post(request):
	passwd=make_password(request.POST.get('password'),'yell','pbkdf2_sha256')
	sales=Sales(sales_name=request.POST.get("sales_name"),sales_mobile=request.POST.get("sales_mobile"),username=request.POST.get("username"),password=passwd)
	sales.save()
	return HttpResponse("REGISTER OK")
	
def register(request):
	template=loader.get_template('crm/register.html')
	return HttpResponse(template.render(RequestContext(request)))



def leads(request):
	customer_list=Customer.objects.order_by('-id')[:5]
	
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
	
		
