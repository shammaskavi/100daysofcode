import datetime as dt 
import smtplib

myEmail = "theyoungvoyager010@gmail.com"
password = "hallelujah"
senderEmail = "wandamaximoff2308@gmail.com"

currentData = dt.datetime.now()
currentday = currentData.strftime("%a").lower()