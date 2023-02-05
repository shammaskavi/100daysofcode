numbers = [1,2,3]
new_list = [n+1 for n in numbers]
print(new_list)

name = "Angela"
letters_list = [letter for letter in name]
print(letters_list)

range_list = [num*2 for num in range(1,5)]
print(range_list)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [n for n in names if len(n) <= 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)