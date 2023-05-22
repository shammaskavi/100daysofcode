import turtle, pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("./50_states.csv")
# data["state"]
all_states = data.state.tolist()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(f"{len(guessed_states)}/50 States Correct", "What's another state").title()
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
screen.title("You guessed all the states, Game Over")
screen._write(pos = (0,0), txt = "Game Over", align = "center", font = ("Arial", 40, "normal"), pencolor="green")
# screen._write(pos = (0,0), txt = "Game Over", align = "center", font = "Arial", pencolor = "red")


screen.exitonclick()