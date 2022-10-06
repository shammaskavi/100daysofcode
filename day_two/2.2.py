# BMI = weight(kg) / height*2

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

bmi = int(weight) / float(height) ** 2

print(f"Your Body Mass Index(BMI) is {round(bmi, 2)} and")


if bmi < 18.5:
    print("You are underweight")
elif bmi > 18.5 and bmi < 25:
    print("You are Normal Weight")
elif bmi > 25 and bmi < 30:
    print("You are Over Weight")
elif bmi > 30:
    print("You are Obese")


# floor division // -  this divides the int and returns the data type of int
# print(type(3/5)) - returns float
# print(type(3//5)) - returns int

# num = 4 / 2
# num /= 2
# print(num)
