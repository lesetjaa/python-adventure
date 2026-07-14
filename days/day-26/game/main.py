import turtle
import pandas


def font(size):
    return ('Courier', size, 'normal')


screen = turtle.Screen()
screen.title("US states Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


def get_mouse_click_coord(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coord)

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()


correct_guesses = []
game_is_on = len(correct_guesses) < 50
while game_is_on:
    answer = screen.textinput(
        title=f"{len(correct_guesses)}/50 States Correct.", prompt="Whats another state's name?").title() # type: ignore

    if answer == "Exit":
        # TODO - use list comprehension
        missing_states = [state for state in states_list if state not in correct_guesses]

        # missing_states = []
        # # for state in states_list:
        # #     if state not in correct_guesses:
        # #         missing_states.append(state)
        states_to_learn = pandas.DataFrame(missing_states)
        states_to_learn.to_csv("../resources/states_to_learn.csv")
        break

    if answer in states_list:
        # since this returns a series, use .item() to get the value
        x_val = data[data["state"] == answer].x.item()
        y_val = data[data["state"] == answer].y.item()

        state = turtle.Turtle(visible=False)
        state.penup()
        state.goto((x_val, y_val))
        state.write(answer, font=font(8))
        correct_guesses.append(answer)

# states_to_learn.csv
