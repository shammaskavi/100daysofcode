total = 0
def add(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

sum = add(2,3,5,6, 21,23,34,45)
print(sum)

def calculator(**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)
        
    print(kwargs['add'])

calculator(add= 3, multiply = 5)

def calc(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)

calc(2, add= 4, multiply = 3)
