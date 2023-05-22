lato_list = {
    "alphabets": ['a', 'b', 'c', 'd', 'e', 'f','g','h','i','j','k','l','m','n','o','p','q','r','s','t', 'u','v','w','x','y','z'],
    "lato" : ["Alpha","Bravo","Charlie","Delta", "Echo","Foxtrot", "Golf","Hotel","India","Juliett",
"Kilo",
"Lima",
"Mike",
"November",
"Oscar",
"Papa", 
"Quebec",
"Romeo",
"Sierra",
"Tango",
"Uniform",
"Victor",
"Whiske", 
"X-ray",
"Yankee", 
"Zulu" ,],
}

name_nato = []
name = input("Enter your name: ")
print(f"Hellow {name}")

for name_letter in name:
    name_nato.append(lato_list[name_letter.lower()])

print(name_nato)

