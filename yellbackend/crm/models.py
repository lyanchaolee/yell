from django.db import models

# Create your models here.

class Customer(models.Model):
	name=models.CharField(max_length=16,null=True)
	nick_name=models.CharField(max_length=16,null=True)
	mobile_no=models.CharField(max_length=16,null=True)
	address=models.CharField(max_length=128,null=True)
	gender=models.CharField(max_length=1,null=True)
	create_time = models.DateTimeField('create time',null=True)
	modified_time = models.DateTimeField('modified time',null=True)
	age=models.IntegerField(null=True)
	is_expr=models.CharField(max_length=1,null='N')
	is_appoints=models.CharField(max_length=1,null='N')
	expr_time=models.DateTimeField('expr time',null=True)
	teacher_name=models.CharField(max_length=16,null=True)
	sales_id=models.BigIntegerField(null=True)
	appoints_time=models.DateTimeField('appoints time',null=True)
	is_service=models.CharField(max_length=1,null='N')
	
class Remark(models.Model):
	refer_type=models.CharField(max_length=16,null=True)
	refer_id=models.BigIntegerField(null=True)
	remark_time=models.DateTimeField(null=True)
	remark=models.CharField(max_length=512,null=True)

class Teacher(models.Model):
	teacher_name=models.CharField(max_length=16,null=True)
	teacher_mobile=models.CharField(max_length=16,null=True)
	
class Sales(models.Model):
	sales_name=models.CharField(max_length=16,null=True)
	sales_mobile=models.CharField(max_length=16,null=True)
	username=models.CharField(max_length=16,null=True)
	password=models.CharField(max_length=128,null=True)
	is_super=models.CharField(max_length=1,null=True)
	
class CustInService(models.Model):
	name=models.CharField(max_length=16,null=True)
	nick_name=models.CharField(max_length=16,null=True)
	mobile_no=models.CharField(max_length=16,null=True)
	address=models.CharField(max_length=128,null=True)
	gender=models.CharField(max_length=1,null=True)
	create_time = models.DateTimeField('create time',null=True)
	modified_time = models.DateTimeField('modified time',null=True)
	age=models.IntegerField(null=True)
	teacher_name=models.CharField(max_length=16,null=True)
	sales_id=models.BigIntegerField(null=True)
	birthday=models.DateField('birthday',null=True)
	classtime=models.DateTimeField('classtime',null=True)
	contract_type=models.CharField(max_length=16,null=True)
	contract_time=models.DateTimeField('contract_time',null=True)
	
	

	
	