from turtle import Turtle, Screen

class StateMap(Turtle):
    """
    Represents a turtle object for a U.S. States guessing game.

    Attributes:
        screen (Screen): The screen where the game is displayed.
        answer (str): The guessed state name.
    """

    def __init__(self) -> None:
        """
        Initializes the StateMap object.

        Initializes the Turtle object with the screen background image and title.
        """
        super().__init__(visible=False)
        self.screen: Screen = Screen()
        self.screen.bgpic('./sources/blank_states_img.gif')
        self.screen.title('U.S. States Game')
        self.penup()
        
    def ask_state(self, found: int) -> None:
        """
        Asks the user to input the name of a state.

        Args:
            found (int): The number of states found by the player.
        
        Raises:
            KeyboardInterrupt: If the user interrupts the game.
        """
        self.answer = self.screen.textinput(title=f'Guess the State ({found}/50)', prompt='What is another state\'s name')
        if self.answer:
            self.answer = self.answer.title()
        else:
            raise KeyboardInterrupt('\033[91m Game is over\033[0m')

    def write_state(self, coordinates: tuple) -> None:
        """
        Writes the guessed state name on the screen at the given coordinates.

        Args:
            coordinates (tuple): The coordinates to write the state name.
        """
        self.goto(coordinates)
        self.write(f'{self.answer}', font=("Arial", 8, "normal"))

    def finish(self) -> None:
        """
        Starts the main loop of the game.
        """
        self.screen.mainloop()
