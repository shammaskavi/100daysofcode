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
    isWeekend = True
    print("Add a motivational quote to get you going !")
else:
    isWeekend = False
    print("You don't need motivation, just die already!!")

if isWeekend:
    with open("./quotes.txt") as f:
        contents = f.readlines()
        print(contents[0])