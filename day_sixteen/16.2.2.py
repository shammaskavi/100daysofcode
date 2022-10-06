from prettytable import PrettyTable

table = PrettyTable()

table.add_column(
    "Pokemon Name", ["Pikachu", "Charmendar", "Squirtle"]
)
table.add_column(
    "Type", ["Electric", "Fire", "Water"]
)

print(table)