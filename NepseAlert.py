import requests
from bs4 import BeautifulSoup
import time
import  smtplib,ssl


nep = int(input("ENTER YOUR DESIRED NEPSE VALUE:"))
sen = int(input("ENTER YOUR DESIRED SENSITIVE VALUE:"))
    

while 1==1:

    req = requests.get("http://www.nepalstock.com/stocklive")
    soup = BeautifulSoup(req.content, "html.parser")
    a = soup.find_all(class_="current-index")
    print(a[0].get_text())
    b = a[0].get_text().split(",")
    c = "".join(b)
    d = float(c)

    if(d > nep):
         print("THE NEPSE IS HIGHER THAN YOU WANT.🔥")
        message="THE NEPSE IS HIGHER THAN YOU WANT.🔥"
    else:
         print("THE NEPSE IS BAD.🥲")

    

    # s=soup.find_all(class_="current-index")
    # print(s[0].get_text())
    # g = s[0].get_text().split(",")
    # h = "".join(g)
    # i= float(h)


    # if(i > sen):
    #     print("THE SENSITIVE IS HIGHER THAN YOU WANT.🔥")
    # else:
    #     print("THE SENSITIVE IS BAD.🥲")
    
time.sleep(1)


port = 587  
smtp_server = "smtp.gmail.com"
sender_email = "someone1@gmail.com"    #use your email1
receiver_email = "someone2@gmail.com"    #use your email2
password = input("Enter your password!")

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls(context=context)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
