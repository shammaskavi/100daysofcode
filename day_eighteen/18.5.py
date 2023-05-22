import turtle as t, random
from turtle import Screen

tim = t.Turtle()
t.colormode(255)
screen = Screen()


# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,b,b)
    return random_color

directions = [0, 90, 180, 270]
tim.pensize(9)
tim.speed("fastest")

for i in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))


screen.exitonclick()