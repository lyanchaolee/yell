#!/bin/bash

######django install
python get-pip.py
pip install Django


######mysqlclient-1.3.7 install
python setup.py build
sudo python setup.py install


#####profile config
export DYLD_LIBRARY_PATH=/usr/local/mysql/lib/ 


drop database yell;
CREATE DATABASE yell DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

insert into crm_customer(name,nick_name,mobile_no,address,gender,create_time,modified_time) values('LYC','YCL','18657100339','ÔÃ¶û¸ÖÇÙ','1',now(),now());


insert into crm_sales(sales_name,sales_mobile,password,username) select first_name,'18657100339',password,username from auth_user where username='lyc';

insert into crm_sales(sales_name,sales_mobile,password,username,is_super) select username,1111,password,username,'N' from auth_user where id=3;

https://pypi.python.org/pypi/pytz/#downloads
sudo python setup.py install


https://pypi.python.org/pypi/xlrd
sudo python setup.py install


alter table crm_customer modify expr_time  datetime(6)  Null;
alter table crm_customer modify appoints_time  datetime(6)  Null;


http://127.0.0.1:8000/admin/

python manage.py shell
python manage.py createsuperuser
python manage.py changepassword

create index service_idx on crm_customer(is_service,is_appoints,is_expr);
