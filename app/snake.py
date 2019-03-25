import random

class Snake:
    """Represents snake."""

    def __init__(self, data):
        # TODO
        self.data = data

    def get_head(self):
        """Get position of snake head."""
        return self.data['body'][0]

    def get_directions_safe(self, board):
        """Get a list of directions to move in given the state of the board."""
        directions = []

        head = self.get_head()
        x = head['x']
        y = head['y']
        if board.is_empty(x + 1, y):
            directions.append('right')
        if board.is_empty(x, y + 1):
            directions.append('down')
        if board.is_empty(x - 1, y):
            directions.append('left')
        if board.is_empty(x, y - 1):
            directions.append('up')

        return directions

    def get_directions_closest_pellet(self, board):
        """Get directions towards closest pellet."""
        directions = []

        head = self.get_head()
        x = head['x']
        y = head['y']

        closest_pellet = board.get_closest_pellet(head)

        cx = closest_pellet['x']
        cy = closest_pellet['y']

        if x - cx > 0:
            directions.append('left')
        elif x - cx < 0:
            directions.append('right')

        if y - cy > 0:
            directions.append('up')
        elif y - cy < 0:
            directions.append('down')

        return directions

