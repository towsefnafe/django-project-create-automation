import sys
import os
import webbrowser

project_name = sys.argv[1]
project_name = project_name.replace(' ', '_')

os.chdir('E://Nafe//project//django')
os.mkdir(project_name)
os.chdir('E://Nafe//project//django//' + project_name)
os.system('virtualenv venv')
os.chdir('E://Nafe//project//django//' + project_name + '//venv//Scripts')
os.system('activate')
os.system('pip install django')
os.chdir('E://Nafe//project//django//' + project_name)
os.system('django-admin startproject ' + project_name)
os.chdir('E://Nafe//project//django//' + project_name + '//' + project_name)
os.system('python manage.py startapp main')
os.system('python manage.py migrate')
webbrowser.open('http://127.0.0.1:8000/')
os.system('python manage.py runserver')

