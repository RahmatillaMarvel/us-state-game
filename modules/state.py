import pandas as pd
from modules.state_map import StateMap
from typing import Union, Tuple

class State(StateMap):
    """
    Represents a state in the U.S. States guessing game.

    Attributes:
        __data (DataFrame): The DataFrame containing state data.
        found_states (int): The number of states found by the player.
    """
    def __init__(self) -> None:
        """
        Initializes the State object.

        Reads state data from CSV file and initializes found_states counter.
        """
        super().__init__()
        self.__data: pd.DataFrame = pd.read_csv('./sources/50_states.csv')
        self.found_states: int = 0
    
    def get_coordinates(self) -> Union[Tuple[int, int], None]:
        """
        Retrieves the coordinates of the guessed state.

        Returns:
            Union[Tuple[int, int], None]: The coordinates of the state, or None if not found.
        """
        x = self.__data[self.__data.state == self.answer].x
        y = self.__data[self.__data.state == self.answer].y
        if x.empty or y.empty:
            return None
        self.found_states += 1
        return (x.iloc[0], y.iloc[0])
