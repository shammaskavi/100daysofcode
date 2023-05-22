import turtle, pandas

screen = turtle.Screen()
screen.title("US State Names")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data_set = pandas.read_csv("./50_states.csv")
state_list = data_set["state"]
answered_state = []

total_states = len(state_list)
guessed_states = 0

while total_states >= guessed_states:
    answer_state = screen.textinput(title=f"Guess The State {guessed_states}/{total_states}", prompt="Name another state.").title()
    print(answer_state)
    
    for state in state_list:
        if answer_state.lower().strip() not in state.lower().strip():
            pass
        else:
            if answer_state in answered_state:
                pass
            else:
                answered_state.append(answer_state)
                guessed_states += 1
                print(answered_state)
                t = turtle.Turtle()
                t.hideturtle()
                t.penup()
                state_data = data_set[data_set.state == answer_state]
                t.goto(int(state_data.x), int(state_data.y))
                t.write(answer_state)


