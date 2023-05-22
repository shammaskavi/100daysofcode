from turtle import Turtle, Screen

tim = Turtle()
screen = Screen() 

def move_forward():
    tim.forward(10)
    print(tim.pos())

def move_backward():
    tim.backward(10)
    print(tim.pos())

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
    print(tim.pos())

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
    print(tim.pos())

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_right, "a")
screen.onkey(turn_left, "d")
screen.onkey(clear, "c")
screen.exitonclick()