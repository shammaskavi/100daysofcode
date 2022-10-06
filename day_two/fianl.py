print("Welcome to the tip calculator")
totalBill = int(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15: "))
tipAmmount = tip * 12 // 100
noOfPeople = int(input("How many people to split the bill? "))
# print(type(tipAmmount))
billAmmount = totalBill + tip
ammountPerPerson = billAmmount / noOfPeople
print(f"Each person should pay: ${ammountPerPerson}")
