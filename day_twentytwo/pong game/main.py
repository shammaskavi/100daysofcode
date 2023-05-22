from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong")

p1=Turtle()
p1.penup()
p1.shape(name="square")
p1.color("white")
p1.shapesize(stretch_wid=5, stretch_len=1) 
p1.goto(350,0)


def go_up():
    new_y = p1.pos()[1] +10
    p1.goto(p1.xcor(), new_y)


def go_down():
    p1.goto(350, p1.pos()[0]-2)


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")


screen.exitonclick()