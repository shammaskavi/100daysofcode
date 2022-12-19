import pandas

data = pandas.read_csv("./weather_data.csv")
print(type(data))
print(type(data["temp"]), end="\n\n\n")

data_dict = data.to_dict()
print(data_dict, end="\n \n \n")

temp_list = data["temp"].tolist()
print(len(temp_list))

# wAY 1 TO FIND AVERAGE OF THE GIVEN LIST DATA
total_temp = 0
for temp in temp_list:
    total_temp+= temp
average_temp = total_temp / len(temp_list) 
print(average_temp, end="\n\n\n")


# WAY 2 OF FINDING THE AVERAGE OF THE GIVEN LIST DATA
average = sum(temp_list) / len(temp_list)
print(average)

# way 3 of finding the average of the given data 
avg = data["temp"].mean()
print(avg)

# max value of the temp column
maxin = data["temp"].max()
print(maxin, end="\n\n\n")


# Accessing column values 
print(data["condition"], end="\n\n\n")
print(data.day, end="\n\n\n")
print(data["temp"], end="\n\n\n")


# Accessing Row values:
x = data[data.day == "Monday"]
print(x, end="\n\n\n")

y = data[data.temp == maxin]
print(y)

monday = data[data.day == "Monday"]
print(monday.condition)
m_cel = int(monday.temp)
print(m_cel)
m_far = (m_cel * 9/5) + 32
print(m_far)


# Create a datafram from scratch
data_dict = {
    "students": ["Ammy", "James", "Angela", "Shammas", "Abdullah"]
    ,"scores": [12, 14, 10, 15, 20] 
}
data_dict_table = pandas.DataFrame(data_dict)
data_dict_table.to_csv("new_data.csv")