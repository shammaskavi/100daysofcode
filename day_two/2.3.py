# wait but why
age = input("What is your current age: ")
remainingAge = 90 - int(age)  # 12 - 90
noOfDays = remainingAge * 365
noOfWeeks = noOfDays // 7
noOfMonths = noOfDays // 30.417

print(f"You have {noOfDays} days, {noOfWeeks} weeks, {noOfMonths} months left..")


# another way
# noOfDays = remainingAge * 365
# noOfWeeks = remainingAge * 52
# noOfMonths = remainingAge * 12
