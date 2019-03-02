import random

class Snake:
    """Represents snake."""

    def __init__(self, data):
        # TODO
        self.data = data

    def get_head(self):
        """Get position of snake head."""
        return self.data['body'][0]

    def get_possible_moves(self, game_board):
        """Get a list of directions to move in given the state of the board."""
        directions = []

        head = self.get_head()
        x = head['x']
        y = head['y']
        if game_board.is_empty(x + 1, y):
            directions.append('right')
        if game_board.is_empty(x, y + 1):
            directions.append('down')
        if game_board.is_empty(x - 1, y):
            directions.append('left')
        if game_board.is_empty(x, y - 1):
            directions.append('up')

        return random.choice(directions)