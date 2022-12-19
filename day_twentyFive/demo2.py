# csv: comma seperated values
import csv


with open("./weather_data.csv") as data_file:
    data = csv.reader(data_file)
    tempertatures = [] 
    for temperature in data:
        if temperature[1] != "temp":
            tempertatures.append(int(temperature[1]))
    print(tempertatures)
                
