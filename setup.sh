#!/bin/bash

#setup virtual environment
virtualenv env
source env/bin/activate
#install all dependancies
pip install -r requirements.txt
#start the server
python run.py