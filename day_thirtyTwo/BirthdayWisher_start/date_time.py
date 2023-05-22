import datetime as dt

x = dt.datetime.now()

print(x)
print(x.year)

# DumDum this is important: 
# This prints the current day (MOnday, Tuesday ....
print(x.strftime("%A"))

# Creating a Date Object 
y = dt.datetime(2003, 7, 11)
# in the format yyyy-mm-dd

print(y)
print(y.strftime("%A")) #Weekday full version ie: Tuesday
print(y.strftime("%B")) #Weekday full version: August
print(y.strftime("%C")) #I don't see how it is useful but it give "Century": 20th(Century fox)