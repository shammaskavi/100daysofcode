from turtle import Turtle, Screen
import random


screen = Screen() 

screen.setup(width=1000, height=400)
user_bet = screen.textinput(title = "Make your Bet", prompt = "Which turtle will win the race ? Enter a color: ")
y_pos = [-70, -40, -10, 20, 50, 80]
colors = ["red", "blue", "pink", "yellow", "green", "purple"]
all_turtle = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.speed("fast")
    new_turtle.color(colors[turtle_index]) 
    new_turtle.penup()
    # new_turtle.goto(-470, turtle_index*30)
    new_turtle.goto(x = -470, y = y_pos[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 470:
            is_race_on = False
            winner = turtle.color()
        rand_dist = random.randint(1,10)
        turtle.forward(rand_dist)
    
if winner[0] == user_bet:
    print("You win")
else:
    print(f"You loose, {winner[0]} color wins")

screen.exitonclick()