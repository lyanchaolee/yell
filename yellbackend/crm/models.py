from django.db import models

# Create your models here.

class Customer(models.Model):
	name=models.CharField(max_length=16)
	nick_name=models.CharField(max_length=16)
	mobile_no=models.CharField(max_length=16)
	address=models.CharField(max_length=128)
	gender=models.CharField(max_length=1)
	create_time = models.DateTimeField('create time')
	modified_time = models.DateTimeField('modified time')
	age=models.IntegerField()
	is_expr=models.CharField(max_length=1)
	is_appoints=models.CharField(max_length=1)
	expr_time=models.DateTimeField('expr time')
	teacher_name=models.CharField(max_length=16)
	sales_id=models.BigIntegerField()
	
class Remark(models.Model):
	refer_type=models.CharField(max_length=16)
	refer_id=models.BigIntegerField()
	remark_time=models.DateTimeField()
	remark=models.CharField(max_length=512)

class Teacher(models.Model):
	teacher_name=models.CharField(max_length=16)
	teacher_mobile=models.CharField(max_length=16)
	
class Sales(models.Model):
	sales_name=models.CharField(max_length=16)
	sales_mobile=models.CharField(max_length=16)
	username=models.CharField(max_length=16)
	password=models.CharField(max_length=128)
	is_super=models.CharField(max_length=1)
	

	
	