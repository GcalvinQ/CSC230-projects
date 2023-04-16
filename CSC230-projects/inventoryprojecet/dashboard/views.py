from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import models
from booking_app.views import userPanel

# Create your views here.

@login_required(login_url='user-login')
def staff(request):
    return render(request, 'dashboard/staff.html')

@login_required(login_url='user-login')
def product(request):
    return render(request, 'dashboard/product.html')

@login_required(login_url='user-login')
def order(request):
    return render(request, 'dashboard/order.html')
