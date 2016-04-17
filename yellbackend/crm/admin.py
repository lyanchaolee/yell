from django.contrib import admin

# Register your models here.

from .models import Customer
from .models import Teacher
from .models import Remark

admin.site.register(Customer)
admin.site.register(Teacher)
admin.site.register(Remark)
