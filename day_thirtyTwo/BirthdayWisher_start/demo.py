import smtplib

myEmail = 'theyoungvoyager010@gmail.com'
password = 'hallelujah'
senderEmail = "wandamaximoff2308@gmail.com"

#Turn on Two step verification for the sender's email account




connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=myEmail, password=password)
connection.sendmail(from_addr= myEmail, to_addrs=myEmail , msg="A note to self")
connection.close()