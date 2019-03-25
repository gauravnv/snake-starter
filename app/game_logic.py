import random

from .snake import Snake
from .board import Board


def get_next_move(board_width, board_height, food, snake, enemies):
    """Return next best move for the given snake."""
    board = Board(board_width, board_height, food, snake, enemies)
    snake = Snake(snake)

    food_directions = snake.get_directions_closest_pellet(board)
    possible_directions = snake.get_directions_safe(board)

    moves = list(set(food_directions) & set(possible_directions))
    move = 'up'
    if moves:
        move = random.choice(moves)
    elif possible_directions:
        move = random.choice(possible_directions)

    return move
