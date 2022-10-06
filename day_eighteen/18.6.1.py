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
    color = (r,b,b)
    return color


tim.speed("fastest")
for i in range(45):
    tim.color(random_color())
    tim.right(8)
    tim.circle(100)


screen.exitonclick()