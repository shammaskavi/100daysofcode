data = []

# with open("./weather_data.csv") as weather_data:
#     for dat in weather_data:
#         print(f"With the for loop, the data type is {type(dat)}")
#     wetdat = weather_data.read()
#     print(f"With the .read() the data type is {type(wetdat)}")



with open("./weather_data.csv") as weather_data:
    for dat in weather_data:
        print(dat) 

print("------------------------------------------------------\n")
with open("./weather_data.csv") as weather_data:
    for cell in weather_data:
        data.append(cell)
print(data)


print("------------------------------------------------------\n")
with open("./weather_data.csv") as wetdat:
    data = wetdat.readlines()
print(data)