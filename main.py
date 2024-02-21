from modules.state import State

# Create an instance of the State class
state = State()

# Loop until all 50 states are found
while state.found_states != 50:
    # Ask the user to input the name of a state
    state.ask_state(state.found_states)
    
    # Get the coordinates of the guessed state
    coordinates = state.get_coordinates()
    
    # If the coordinates are found, write the state name on the screen
    if coordinates:
        state.write_state(coordinates)

# Finish the game
state.finish()
