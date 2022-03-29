from django.shortcuts import render
from django.http import HttpResponse
import pyodbc
email=""
u="'"
fname=""
lname=""
space=" "
comma=","
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=server_name;'
                      'Database=database_name;'
                      'Trusted_Connection=yes;')
# uii=conn.execute("select * from Orders")    
# res=uii.fetchall()
# print(res)
# Create your views here.
def index(request):
    return render (request,'app1/home.html')
def check(request):

    fname=str(request.GET['fname'])
    lname=str(request.GET['lname'])
    email=str(request.GET['email'])
    password=str(request.GET['password'])
    import random
    import smtplib
    #passlen = int(input("Enter the length of the  password "))
    passlen =5
    s="ASDFGHJKLMNBVCXZPOIUYTREWQ1234567890"
    otp_pass=str("".join(random.sample(s,passlen)))# generating otp
    # print(otp_pass)
    server=smtplib.SMTP(host='smtp.gmail.com',port=587) 
    server.ehlo()
    server.starttls()
    server.login("123@gmail.com","password of 123@gmail.com")
    subject = 'YOUR VERIFICATION CODE'
    body=otp_pass
    message = f'Subject :{subject} \n\n {body}'

    server.sendmail('123@gmail.com',email,message)
    server.quit()

    sql= "INSERT INTO [dbo].[email_verify]([fname],[lname],[email],[password],[otp]) VALUES("+u+fname+u+comma+u+lname+u+comma+u+email+u+comma+u+password+u+comma+u+otp_pass+u+")"
    # sql=",".join("")  
    # print(sql)          
    cursor = conn.cursor()
    cursor.execute(str(sql))
    conn.commit()
    return render(request,'app1/otp.html')

def login_page(request):
    return render(request,'app1/login.html')
def  sign_up_page(request):
    return render(request,'app1/home.html')
def verify(request):
    data=request.GET['otp']
    sql= ("SELECT  otp FROM [dbo].[email_verify] WHERE email="+u+email+u)
    cursor = conn.cursor()
    cursor.execute(sql)
    yu=cursor.fetchall()
    yu=str(yu)
    yu=yu.replace(",","")
    yu=yu.replace("(","")
    yu=yu.replace(")","")
    yu=yu.replace("[","")
    yu=yu.replace("]","")
    yu=yu.replace("'","")
    yu=yu.strip()
    conn.commit()
    if data==yu:
            sql2= ("select fname from [dbo].[email_verify] where [email]="+u+email+u)
            cursor = conn.cursor()
            cursor.execute(sql2)
            fname_1=cursor.fetchall()
            fname_1=str(fname_1)
            fname_1=fname_1.replace(",","")
            fname_1=fname_1.replace("(","")
            fname_1=fname_1.replace(")","")
            fname_1=fname_1.replace("[","")
            fname_1=fname_1.replace("]","")
            fname_1=fname_1.replace("'","")
            fname=fname_1.strip()
            fname=fname_1.upper()
            sql3= ("select lname from [dbo].[email_verify] where [email]="+u+email+u)
            cursor = conn.cursor()
            cursor.execute(sql3)
            fname_2=cursor.fetchall()
            fname_2=str(fname_2)
            fname_2=fname_2.replace(",","")
            fname_2=fname_2.replace("(","")
            fname_2=fname_2.replace(")","")
            fname_2=fname_2.replace("[","")
            fname_2=fname_2.replace("]","")
            fname_2=fname_2.replace("'","")
            lname=fname_2.strip()
            lname=fname_2.upper()
            name=fname+space+lname
            conn.commit()
            return (request,'app1/dashboard.html',{'name':name})
    else:
        return render (request,'app1/home.html')
def login_check(request):
    email=request.GET['email']
    #print(email)
    password=request.GET['password']
    #print(password)
    sql= ("select password from [dbo].[email_verify] where [email]="+u+email+u)
     
    #print(sql)          
    cursor = conn.cursor()
    cursor.execute(sql)
    yuu=cursor.fetchall()
    yuu=str(yuu)
    yuu=yuu.replace(",","")
    yuu=yuu.replace("(","")
    yuu=yuu.replace(")","")
    yuu=yuu.replace("[","")
    yuu=yuu.replace("]","")
    yuu=yuu.replace("'","")
    yuu=yuu.strip()
    #print(yuu)
    sql2= ("select fname from [dbo].[email_verify] where [email]="+u+email+u)
    cursor = conn.cursor()
    cursor.execute(sql2)
    fname_1=cursor.fetchall()
    fname_1=str(fname_1)
    fname_1=fname_1.replace(",","")
    fname_1=fname_1.replace("(","")
    fname_1=fname_1.replace(")","")
    fname_1=fname_1.replace("[","")
    fname_1=fname_1.replace("]","")
    fname_1=fname_1.replace("'","")
    fname=fname_1.strip()
    fname=fname_1.upper()
    sql3= ("select lname from [dbo].[email_verify] where [email]="+u+email+u)
    cursor = conn.cursor()
    cursor.execute(sql3)
    fname_2=cursor.fetchall()
    fname_2=str(fname_2)
    fname_2=fname_2.replace(",","")
    fname_2=fname_2.replace("(","")
    fname_2=fname_2.replace(")","")
    fname_2=fname_2.replace("[","")
    fname_2=fname_2.replace("]","")
    fname_2=fname_2.replace("'","")
    lname=fname_2.strip()
    lname=fname_2.upper()
    conn.commit()
    if yuu== password:
        name=fname+space+lname
        #print(name)
        return render (request,'app1/dashboard.html',{'name':name})
    else:
        return render (request,'app1/home.html')

    
def login_out(request):
    return render (request,'app1/home.html')