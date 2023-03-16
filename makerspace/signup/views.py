from django.shortcuts import render, redirect
import mysql.connector as sql
import hashlib

fn = ''
ln = ''
u = ''
em = ''
pwd = ''



# Create your views here.
def signaction(request):
    global fn, ln, u, em, pwd
    if request.method == "POST":
        m=sql.connect(host = 'localhost', user='root', passwd='', database='makerspace')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="firstName":
                fn = value
            if key=="lastName":
                ln = value
            if key=="user_name":
                u = value
            if key=="email":
                em = value
            if key=="password":
                pwd = value
        passwordHash = hashlib.sha256(pwd.encode('utf-8')).hexdigest()
        c="insert into account Values('{}', '{}', '{}', '{}', '{}')".format(fn, ln, u, em, passwordHash)
        cursor.execute(c)
        m.commit()
        return redirect('http://127.0.0.1:8000/login')
        
    
    return render(request,'signup_page.html')