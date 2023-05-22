import datetime as dt 
import smtplib

#Constants:
myEmail = "theyoungvoyager010@gmail.com"
password = "hallelujah"
senderEmail = "wandamaximoff2308@gmail.com"

currentData = dt.datetime.now()
currenDay = currentData.strftime("%a").lower()
print(currenDay)
if currenDay == "sat":
    print("It is saturday you dummy")
else:
    print("It is not saturday, but you sir are dummy for sure")