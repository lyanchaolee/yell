from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader,RequestContext
from .models import Customer
from .models import Remark
from .models import Sales
from .models import CustInService
from django.contrib.auth.hashers import make_password,check_password
from django.core.urlresolvers import reverse
from django.contrib.auth.views import logout as django_logout
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
import xlrd

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
		filter_type=request.GET["filter_type"]
	except(KeyError):
		filter_type='all'
	if filter_type ==None or filter_type=='':
		filter_type='all'
	try:
		sales_identify=request.COOKIES["user_id"]

		sales=Sales.objects.get(id=sales_identify)
		if sales.is_super=='Y':
			if filter_type=='all':
				customer_list=Customer.objects.filter(is_service='N').order_by('-modified_time')
			elif filter_type=='new':
				customer_list=Customer.objects.filter(is_expr='N',is_appoints='N',is_service='N').order_by('-modified_time')
			elif filter_type=='nappoints':
				customer_list=Customer.objects.filter(is_expr='Y',is_appoints='N',is_service='N').order_by('-modified_time')
			else:
				customer_list=Customer.objects.filter(is_expr='Y',is_appoints='Y',is_service='N').order_by('-modified_time')
		else:
			if filter_type=='all':
				customer_list=Customer.objects.filter(sales_id=sales_identify,is_service='N').order_by('-modified_time')
			elif filter_type=='new':
				customer_list=Customer.objects.filter(sales_id=sales_identify,is_expr='N',is_appoints='N',is_service='N').order_by('-modified_time')
			elif filter_type=='nappoints':
				customer_list=Customer.objects.filter(sales_id=sales_identify,is_expr='Y',is_appoints='N',is_service='N').order_by('-modified_time')
			else:
				customer_list=Customer.objects.filter(sales_id=sales_identify,is_expr='Y',is_appoints='Y',is_service='N').order_by('-modified_time')
			
		paginator = Paginator(customer_list, 20)
		page = request.GET.get('page')
		try:
			customer_list = paginator.page(page)
		except PageNotAnInteger:
			customer_list = paginator.page(1)
		except EmptyPage:
			customer_list = paginator.page(paginator.num_pages)
			
		for customer in customer_list:
			c_sales=Sales.objects.get(id=customer.sales_id)
			customer.sales_name=c_sales.sales_name
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
			'filter_type':filter_type,
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
	
def test(request):
	template=loader.get_template('crm/test.html')
	
	return HttpResponse(template.render(request))
	
def lead_editing(request):
	template=loader.get_template('crm/lead_editing.html')
	
	return HttpResponse(template.render(request))
	
def reservation(request):
	customerid=request.GET.get('cust_id')
	customer=Customer.objects.get(id=customerid)
	context={
		'customer':customer
	}
	template=loader.get_template('crm/reservation.html')
	return HttpResponse(template.render(context,request))

	
def resrvation_post(request):
	timeselect=request.POST.get('timeselect')
	customerid=request.POST.get('customerid')
	customer=Customer.objects.filter(id=customerid).update(expr_time=timeselect,modified_time=timezone.now(),is_expr='Y')
	return HttpResponseRedirect('leads.html')

def appoints(request):
	customerid=request.GET.get('cust_id')
	customer=Customer.objects.get(id=customerid)
	context={
		'customer':customer
	}
	template=loader.get_template('crm/appoints.html')
	return HttpResponse(template.render(context,request))	
	
def appoints_post(request):
	timeselect=request.POST.get('timeselect')
	customerid=request.POST.get('customerid')
	customer=Customer.objects.filter(id=customerid).update(appoints_time=timeselect,modified_time=timezone.now(),is_appoints='Y')
	return HttpResponseRedirect('leads.html')
	
def remark(request):
	customerid=request.GET.get('cust_id')
	customer=Customer.objects.get(id=customerid)
	context={
		'customer':customer
	}
	template=loader.get_template('crm/remark.html')
	return HttpResponse(template.render(context,request))	
	
def remark_post(request):
	remark_str=request.POST.get('remark')
	customerid=request.POST.get('customerid')
	remark = Remark(refer_type="Leads",refer_id=customerid,remark=remark_str,remark_time=timezone.now())
	remark.save()
	Customer.objects.filter(id=customerid).update(modified_time=timezone.now())
	return HttpResponseRedirect('leads.html')

def leads_filter(request):
	filter_type=request.GET.get('filter_type')
	return HttpResponseRedirect('leads.html?filter_type='+filter_type)
	
	
def leads_upload(request):
	file_obj=request.FILES['fileupload']
	sales_identify=request.COOKIES["user_id"]
	if file_obj:
		destination = open('/root/yellupload/test.xlsx', 'wb+')
		for chunk in file_obj:
			destination.write(chunk)
		destination.flush()
		destination.close()
		workbook=xlrd.open_workbook('/root/yellupload/test.xlsx')
		sheet=workbook.sheet_by_index(0)
		cust_list=[]
		if sheet:
			nrows=sheet.nrows
			if nrows>1:
				for rownum in range(1,nrows):
					row = sheet.row_values(rownum)
					if len(row) == 7:
						cust_list.append(Customer(name=row[0],nick_name=row[1],mobile_no=str(int(row[2])),
										address=row[3],gender=row[4],create_time=timezone.now(),
									 	modified_time=timezone.now(),age=row[5],is_expr='N',teacher_name=row[6],
									 	sales_id=sales_identify,is_appoints='N',is_service='N'))
				Customer.objects.bulk_create(cust_list)
			return HttpResponseRedirect('leads.html')
	else:
		return HttpResponse("Where is your file")
		
def payment(request):
	customerid=request.GET.get('cust_id')
	customer=Customer.objects.get(id=customerid)
	context={
		'customer':customer
	}
	template=loader.get_template('crm/payment.html')
	return HttpResponse(template.render(context,request))
	
def payment_post(request):
	sales_identify=request.COOKIES["user_id"]
	customerid=request.POST.get('customerid')
	birthday_str=request.POST.get('birthday')
	teachername_str=request.POST.get('teachername')
	contract_type_str=request.POST.get('contract_type')
	contract_type_str=request.POST.get('contract_type')
	classtime_str=request.POST.get('classtime')
	customer=Customer.objects.get(id=customerid)
	cust = CustInService(name=customer.name,nick_name=customer.nick_name,mobile_no=customer.mobile_no,address=customer.address,age=customer.age,
						gender=customer.gender,create_time=timezone.now(),modified_time=timezone.now(),teacher_name=teachername_str,
						sales_id=sales_identify,birthday=birthday_str,classtime=classtime_str,contract_type=contract_type_str,contract_time=timezone.now())
	cust.save()
	Customer.objects.filter(id=customerid).update(is_service='Y',modified_time=timezone.now())
	return HttpResponseRedirect('member.html')


def member(request):
	sales_identify=request.COOKIES["user_id"]
	sales=Sales.objects.get(id=sales_identify)
	if sales.is_super=='Y':
		service_list=CustInService.objects.all()
	else:
		service_list=CustInService.objects.filter(sales_id=sales_identify)
	for service in service_list:
		service.sales_name=Sales.objects.get(id=service.sales_id).sales_name
	template=loader.get_template('crm/member.html')
	context={
		'service_list':service_list
	}
	
	return HttpResponse(template.render(context, request))
