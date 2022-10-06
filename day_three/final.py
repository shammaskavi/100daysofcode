print(
    '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''
)


print("Welcome to Treasure Island.")
print("Your mission is to find the treassure.")
dir = input(
    "You're at corss road. Where do you want to go? Type 'left' or 'right': ")
if dir == "left":
    meansoftrans = input(
        "you came to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across: "
    )

    if meansoftrans == "wait":
        color = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, one blue. Which color do you choose? "
        )
        if color == "red":
            print("Burn by fire. Game Over")
        elif color == "blue":
            print("Eaten by beasts, Game Over")
        elif color == "yellow":
            print("You won")
        else:
            print("Game Over")
    else:
        print("Attacked by trout, Game Over")

elif dir == "right":
    print("You fell into a hole. Game Over.")
