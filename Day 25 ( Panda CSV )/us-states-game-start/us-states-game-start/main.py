import turtle
import pandas
from turtle import Turtle, Screen
from scoreboard import Scoreboard
from scoreboard import ScreenManager

screen = Screen()
scoreboard = Scoreboard()
screen_manager = ScreenManager()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"Guess the State, {scoreboard.score} / 50",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    guessed_states.append(answer_state)
    scoreboard.update_scoreboard()
    if answer_state in all_states:
        state_data = data[data.state == answer_state]
        screen_manager.update_screen(x=int(state_data.x), y=int(state_data.y), name=state_data.state.item())
        scoreboard.increase_score()

missing_states = [state for state in all_states if state not in guessed_states]
learning_data = pandas.DataFrame(missing_states)
learning_data.to_csv("states_to_learn.csv")
screen.mainloop()
