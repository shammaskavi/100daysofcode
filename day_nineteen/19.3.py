from turtle import Turtle, Screen

timmy = Turtle()
tommy = Turtle()


screen = Screen() 

def move_forward():
    timmy.forward(10)

def move_backward():
    timmy.backward(10)

def turn_right():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)

def turn_left():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

# ------------------------------
def move_tom_forward():
    tommy.forward(10)

def move_tom_backward():
    tommy.backward(10)

def turn_tom_right():
    new_heading = tommy.heading() - 10
    tommy.setheading(new_heading)

def turn_tom_left():
    new_heading = tommy.heading() + 10
    tommy.setheading(new_heading)


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_right, "a")
screen.onkey(turn_left, "d")
screen.onkey(clear, "c")
# ---------------------------------------
screen.onkey(move_tom_forward, "Up")
screen.onkey(move_tom_backward, "Down")
screen.onkey(turn_tom_right, "Right")
screen.onkey(turn_tom_left, "Left")
screen.onkey(clear, "x")

screen.exitonclick()
