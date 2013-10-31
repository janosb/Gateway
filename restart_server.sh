#!/bin/bash

kill $(cat $PWD/django.pid)
python manage.py runfcgi method=prefork host=127.0.0.1 port=3033 pidfile=$PWD/django.pid outlog=$PWD/django.out errlog=$PWD/django.err