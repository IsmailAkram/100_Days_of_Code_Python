import pandas as pd
from mapManager import MapManager

MAP_IMAGE = "blank_states_img.gif"
DATA_FILE = "50_states.csv"
MAP_TITLE = "U.S. States Game"

data = pd.read_csv(DATA_FILE)
all_locations = list(data[data.columns[0]]) # list(data.state) or data.state.to_list()
game = MapManager(MAP_TITLE, MAP_IMAGE, DATA_FILE, len(all_locations))

guessed_location = []
prompt_text = "What's another state's name?"

while len(guessed_location) < len(all_locations):
    answer_state = game.screen.textinput(title=f"{len(guessed_location)}/{len(all_locations)} States Correct", prompt=prompt_text)
    if answer_state is None: # "Cancel" causes title() to crash
        break
    answer_state = answer_state.title()
    if answer_state == "Exit":
        # missing_state = []
        # for state in states:
        #     if state not in guessed_location:
        #         missing_state.append(state)
        missing_state = [state for state in all_locations if state not in guessed_location]
        missing_states_to_export = pd.DataFrame(missing_state)
        missing_states_to_export.to_csv("states_to_learn.csv")
        game.show_final_score()
        break

    if answer_state in guessed_location:
        prompt_text = f"You already guessed {answer_state}. Try another one!"
    elif answer_state in all_locations and answer_state not in guessed_location:
        state_xcor = data[data.state == f"{answer_state}"].x.item()
        state_ycor = data[data.state == f"{answer_state}"].y.item()
        # print(state_xcor, state_ycor)
        guessed_location.append(answer_state)
        game.map_state(answer_state, state_xcor, state_ycor)
    else:
        prompt_text = f"{answer_state} isn't a state. Try again!"

