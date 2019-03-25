import random

from .snake import Snake
from .board import Board
from .constants import Directions


def get_next_move(board_width, board_height, food, snake, enemies):
    """Return next best move for the given snake."""
    board = Board(board_width, board_height, food, snake, enemies)
    snake = Snake(snake)

    food_directions = snake.get_moves_closest_pellet(board)
    safe_directions = snake.get_moves_safe(board)

    moves = list(set(food_directions) & set(safe_directions))
    move = Directions.UP
    if moves:
        move = random.choice(moves)
    elif safe_directions:
        move = random.choice(safe_directions)

    return move
