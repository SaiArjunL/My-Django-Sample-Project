from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Users

# Create your views here.

def index(req):
    email_id_list = Users.objects.order_by('email_id')
    email_dict = {'email_id': email_id_list}
    return render(req, 'first_app/index.html', context = email_dict)

def users(req):
    users_list = Users.objects.order_by('first_name')
    name_dict = {'users': users_list}
    return render(req, 'first_app/users.html', context = name_dict)
