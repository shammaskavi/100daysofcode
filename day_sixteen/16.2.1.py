from prettytable import PrettyTable

table = PrettyTable()
table.align = "l"
poke = [
    ["Pickachu", "Electric Type"],
    ["Bulbasaur", "Grass Type"],
    ["Charizad", "Fire Type"],
]

table.field_names = ["Pokemon Name", "Pokemon Type"]
# table
# table.add_row(["Pickachu", "Electric Type"])
# table.add_rows(poke)
table.add_rows(
    [
    ["Pickachu", "Electric Type"],
    ["Bulbasaur", "Grass Type"],
    ["Charizad", "Fire Type"],
]
)

print(table)
