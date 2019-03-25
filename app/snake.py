import random

from .point import Point

class Snake:
    """Represents snake."""

    def __init__(self, data):
        self._body = data['body']

    def _get_head(self):
        """Get position of snake head."""
        return Point.from_json(self._body[0])

    def _get_tail(self):
        """Get position of snake tail."""
        return Point.from_json(self._body[-1])

    def get_directions_safe(self, board):
        """Get a list of directions to move in given the state of the board."""
        head = self._get_head()

        directions = []
        if board.is_empty(head.copy(dx = 1)):
            directions.append('right')
        if board.is_empty(head.copy(dy = 1)):
            directions.append('down')
        if board.is_empty(head.copy(dx = -1)):
            directions.append('left')
        if board.is_empty(head.copy(dy = -1)):
            directions.append('up')

        return directions

    def get_directions_closest_pellet(self, board):
        """Get directions towards closest pellet."""
        head = self._get_head()
        pellet = board.get_closest_pellet(head)

        directions = []
        if head.x - pellet.x > 0:
            directions.append('left')
        elif head.x - pellet.x < 0:
            directions.append('right')

        if head.y - pellet.y > 0:
            directions.append('up')
        elif head.y - pellet.y < 0:
            directions.append('down')

        return directions
