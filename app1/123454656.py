data="bishwajitgarai2gmail.com"
p="46788"
email=""
u="'"
fname='fname'
lname='lname'
email='email'
password='password'
sql= ("INSERT INTO [dbo].[email_verify]([fname],[lname],[email],[password],[otp]) VALUES("+u+fname+u,+u+lname+u,+u+email+u,+u+password+u,u+p+u,")")
sql=",".join(sql)  
print(sql)