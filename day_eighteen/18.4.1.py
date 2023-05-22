from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def draw_triangle(len):
    tim.pencolor("red")
    for i in range(3):
        tim.right(120)
        tim.forward(len)

def draw_square(len):
    tim.pencolor("green")
    for i in range(4):
        tim.right(90)
        tim.forward(len)

def draw_pentagon(len):
    tim.pencolor("blue")
    for i in range(5):
        tim.right(72)
        tim.forward(len)

def draw_hexagon(len):
    tim.pencolor("grey")
    for i in range(6):
        tim.right(60)
        tim.forward(len)

def draw_heptagon(len):
    tim.pencolor("purple")
    for i in range(7):
        tim.right(51.42)
        tim.forward(len)

def draw_octagon(len):
    tim.pencolor("violet")
    for i in range(8):
        tim.right(45)
        tim.forward(len)

def draw_nonagon(len):
    tim.pencolor("orange")
    for i in range(9):
        tim.right(40)
        tim.forward(len)

draw_triangle(100)
draw_square(100)
draw_pentagon(100)
draw_hexagon(100)
draw_heptagon(100)
draw_octagon(100)
draw_nonagon(100)

screen.exitonclick()