#!/bin/bash

#startup redis
nohup /Users/olanre/Documents/SHOP/redis-stable/src/redis-server & ;

#setup virtual environment
virtualenv env
source env/bin/activate
#install all dependancies
pip install -r requirements.txt

#start rabbitmq
rabbitmq-server -detached

#start the celery worker
nohup celery worker -A app/jobs/celery_tasks -l INFO &

#start the server
#python run.py