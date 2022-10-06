import turtle as t, random
from turtle import Screen

tim = t.Turtle()
t.colormode(255)
screen = Screen()
color_list = [(197, 169, 109), (104, 87, 96), (159, 94, 65), (66, 101, 112),(11, 51, 65), (127, 138, 91), (130, 155, 166), (242, 198, 131), (164, 153, 158), (189, 98, 75), (37, 76, 83)]


tim.penup()
tim.shape("triangle")

# To take the turtle pointer to the bottom left of the screen
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

num_of_dots = 100

for dot_count in range(1, num_of_dots+ 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen.exitonclick()