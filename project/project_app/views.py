# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
# from django.shortcuts import get_objects_or_404
from django.db.models import Q
from django.contrib import messages
from django.views.generic import (CreateView,TemplateView,ListView,View)
from . import forms
from .forms import RegiestForm, UserForm
from .models import Regiest_Form
from . import models

# Create your views here.

def search(request):
    if request.method== 'POST':
        srch = request.POST['srh']
        if srch:
            match = Regiest_Form.objects.filter(Q(std_num__icontains=srch))
            if match:
                return render(request, 'project_app/search.html', {'sr':match})
            else:
                messages.error(request,'no result found')
        else:
            messages.error(request,'not found')
    return render(request, 'project_app/search.html')


def payment(request):
    if request.method== 'POST':
        nam = request.POST['name']
        if nam:
            match = Customer_Profile.objects.filter(Q(customer_name__icontains=nam))
            if match:
                return render(request, 'project_app/search.html', {'found':match})
            else:
                messages.error(request,'no result found')
        else:
            messages.error(request,'not found')
    return render(request, 'project_app/search.html')

# password = request.POST['password']
# account_no = request.POST['account_no']
# un_no = request.POST['un_no']
# amount = request.POST['amount']
# form = TransactionForm(request.POST or None)
# if form.is_valid():
# Q(customer_password__icontains=password)|
# Q(customer_number__icontains=account_no)|
# Q(university_number__icontains=un_no)
    # transaction = Transaction()
    # transaction.transaction_amount = transaction.get_total()
    # transaction.save()

# def student_detial_view(request):
    # if request.method == "POST":
    #     std_num = request.POST['std_num']
    #     obj = Regiest_Form.objects.get(std_num)
    #     context = {
    #         'std_name': obj.std_name,
    #         'std_deptart': obj.std_deptart,
    #     }
    # return render(request, "project_app/detail.html", {})



def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'project_app/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'index.html', {})
            else:
                return render(request, 'project_app/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'project_app/login.html', {'error_message': 'Invalid login'})
    return render(request, 'project_app/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'login.html', {})
    context = {
        "form": form,
    }
    return render(request, 'project_app/register.html', context)
