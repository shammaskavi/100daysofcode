from turtle import Turtle, Screen
import random

tim = Turtle()
tim.color("red")
sam = Turtle()
sam.color("yellow")
tom = Turtle()

turt = [tim, sam, tom]

game = True

while game:
    tim.forward(random.randint(1, 10))
    sam.forward(random.randint(1, 10))
    tom.forward(random.randint(1, 10))
    for tut in turt:
        if(tut.pos()== (450.00,0.00)):
            game = False
            print(f"{tut} win the game")



screen = Screen()



screen.exitonclick()