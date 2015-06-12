#!/bin/bash

kill $(cat $PWD/django1.pid)
python manage.py runfcgi method=prefork host=127.0.0.1 port=3033 pidfile=$PWD/django1.pid outlog=$PWD/django1.out errlog=$PWD/django1.err
