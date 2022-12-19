import pandas

data = pandas.read_csv("./squirrel_data.csv")
sql_list = data["Primary Fur Color"]
sql_list.tolist()
print(sql_list[2:])


gray = 0
balck = 0
red = 0
for sql in sql_list[2:]:
    if sql == "Gray":
        gray+= 1
    elif sql == "Cinnamon":
        red+= 1
    elif sql == "Black":
        balck+= 1

new_data = {
    "fur color": ["grey", "red", "black"],
    "count": [gray, red, balck]
}

new_data_dict = pandas.DataFrame(new_data)
new_data_dict.to_csv("result.csv")