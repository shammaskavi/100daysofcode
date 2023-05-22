# Lists
import random

names = input("Enter the names of people seperated by a ,: ")
namesList = names.split(",")
person = namesList[random.randint(0, len(namesList) - 1)]

print(f"{person} will pay the bill")
namesList.append("fuck")
print(namesList)
