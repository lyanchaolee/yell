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
	
	


	
	