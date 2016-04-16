#!/bin/bash

######django install
python get-pip.py
pip install Django


######mysqlclient-1.3.7 install
python setup.py build
sudo python setup.py install


#####profile config
export DYLD_LIBRARY_PATH=/usr/local/mysql/lib/ 