from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.listen()
def move_forward():
    tim.forward(5)


# use methods when using predefined methods/functions
screen.onkey(fun = move_forward, key = "w")
# when the function is passed as parameter, paranthesis are not added after the func calling


screen.exitonclick()