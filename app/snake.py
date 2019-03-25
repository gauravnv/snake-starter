import random

from .point import Point
from .constants import Directions

class Snake:
    """Represents snake."""

    def __init__(self, data):
        self._body = data['body']

    def get_head(self):
        """Get position of snake head."""
        return Point.from_json(self._body[0])

    def get_tail(self):
        """Get position of snake tail."""
        return Point.from_json(self._body[-1])

    def get_moves_safe(self, board):
        """Get a list of directions to move in given the state of the board."""
        head = self.get_head()

        directions = []
        if board.is_empty(head.copy(dx = 1)):
            directions.append(Directions.RIGHT)
        if board.is_empty(head.copy(dy = 1)):
            directions.append(Directions.DOWN)
        if board.is_empty(head.copy(dx = -1)):
            directions.append(Directions.LEFT)
        if board.is_empty(head.copy(dy = -1)):
            directions.append(Directions.UP)

        return directions

    def get_moves_to_tail(self, board):
        """Get directions towards tail."""
        head = self.get_head()
        tail = self.get_tail()

        return head.get_directions_to(tail)

    def get_moves_to(self, board, point):
        """Get directions towards closest pellet."""
        head = self.get_head()

        return head.get_directions_to(point)

    def get_distance_from(self, board, point):
        """Get Manhattan distance of head from given point."""
        head = self.get_head()

        return Point.get_manhattan_distance(head, point)
