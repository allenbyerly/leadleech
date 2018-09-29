#!/bin/sh
cd -- "$(dirname "$BASH_SOURCE")"

#Install pip
sudo easy_install pip
pip install --user --upgrade pip

#Install virtualenv
sudo pip install virtualenv

#Create a virtual environment
virtualenv env

#Activate vitrual environment
source env/bin/activate

#Install packages
pip install bs4
pip install requests
pip install pandas

#Deactivate virtual environment
deactivate
