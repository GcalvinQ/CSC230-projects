from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import mysql.connector as sql

# Create your views here.
def index(request):
    m=sql.connect(host = 'localhost', user='root', passwd='', database='makerspace')
    cursor=m.cursor()
    
    return render(request, 'welcome.html')