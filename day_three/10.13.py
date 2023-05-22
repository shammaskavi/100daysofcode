def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def is_even(number):
    if number % 2 == 0:
        return True


def days_in_month(year, month):
    if is_leap(year) and month == 2:
        return 29
    elif not is_leap(year) and month == 2:
        return 28
    elif not is_even(month):
        return 31
    elif month != 2 and is_even(month):
        return 30


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
