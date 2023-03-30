from django.shortcuts import render, redirect, reverse
import mysql.connector as sql
import hashlib

u = ''
pwd = ''



# Create your views here.
def loginaction(request):
    global u, pwd
    if request.method == "POST":
        m=sql.connect(host = 'localhost', user='root', passwd='', database='makerspace')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="user_name":
                u = value
            if key=="password":
                pwd = value
        passwordDecode = hashlib.sha256(pwd.encode('utf-8')).hexdigest()
        c="select * from account where username='{}' and password='{}'".format(u, passwordDecode)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            j = "update account set is_loggedIn = {} where username = '{}' and password = '{}' and is_loggedIn = {}".format(1, u, passwordDecode, 0)
            cursor.execute(j)
            m.commit()
            return redirect('http://127.0.0.1:8000/dashboard')
    
    return render(request,'login_page.html')