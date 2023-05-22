from withDict import lato_list
import pandas

lato_list_csv = pandas.DataFrame(lato_list)
lato_list_csv.to_csv("latoList.csv")

print(lato_list_csv)