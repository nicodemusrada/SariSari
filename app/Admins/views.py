from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Admins
from pprint import pprint
from django.views.generic import View

def index(request):
    if 'logged_in' in request.session and request.session['logged_in'] == True:
        return redirect('/home')
    else:
        return redirect('/users/login')

class Login(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        sAdminName = request.POST['admin_name']
        sAminPass = request.POST['admin_password']
        bValidAdmin = Admins.validatePassword(sAdminName, sAminPass)
        if bValidAdmin == False:
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})
        request.session['logged_in'] = True
        request.session['admin_name'] = sAdminName
        return redirect('/home')