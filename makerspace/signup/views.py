from django.shortcuts import render
import mysql.connector as sql
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
        
        c="insert into account Values('{}', '{}', '{}', '{}', '{}')".format(fn, ln, u, em, pwd)
        cursor.execute(c)
        m.commit()
    
    return render(request,'signup_page.html')