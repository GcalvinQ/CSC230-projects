from django.shortcuts import render
import mysql.connector as sql
import hashlib
em = ''
pwd = ''



# Create your views here.
def loginaction(request):
    global em, pwd
    if request.method == "POST":
        m=sql.connect(host = 'localhost', user='root', passwd='', database='makerspace')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em = value
            if key=="password":
                pwd = value
        passwordDecode = hashlib.sha256(pwd.encode('utf-8')).hexdigest()
        c="select * from account where email='{}' and password='{}'".format(em, passwordDecode)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request, 'welcome.html')
    
    return render(request,'login_page.html')