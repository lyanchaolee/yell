from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader,RequestContext
from .models import Customer
from .models import Remark
from .models import Sales
from django.contrib.auth.hashers import make_password,check_password
from django.core.urlresolvers import reverse
from django.contrib.auth.views import logout as django_logout
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



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
	
def sign_out(request):

	response = django_logout(request,next_page='login.html')

	response.delete_cookie('user_id')
	
	return response


def login_post(request):
	sales=Sales.objects.get(username=request.POST.get('username'))
	passinput=request.POST.get('password')
	if check_password(passinput,sales.password):
		response=HttpResponseRedirect('leads.html')
		response.set_cookie("is_login","True")
		response.set_cookie("user_id",sales.id)
		return response
	else:
		return HttpResponse("LOGIN FAIL"+sales.password+passinput)


def leads(request):
	try:
		sales_identify=request.COOKIES["user_id"]
		sales=Sales.objects.get(id=sales_identify)
		if sales.is_super=='Y':
			customer_list=Customer.objects.order_by('-id')
		else:
			customer_list=Customer.objects.filter(sales_id=sales_identify).order_by('-id')
		paginator = Paginator(customer_list, 20)
		page = request.GET.get('page')
		try:
			customer_list = paginator.page(page)
		except PageNotAnInteger:
			customer_list = paginator.page(1)
		except EmptyPage:
			customer_list = paginator.page(paginator.num_pages)
			
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
		
		page_list=[]
		for i in range(1,customer_list.paginator.num_pages+1):
			page_list.append(i)
		
		context={
			'customer_list':customer_list,
			'page_list':page_list,
			'sales_id':sales_identify,
		}
		return HttpResponse(template.render(context, request))
	except(KeyError):
		return HttpResponse("You don't have privileges")		


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
	
		
