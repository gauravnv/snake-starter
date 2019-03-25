from .snake import Snake
from .board import Board
from .constants import Directions


def get_next_move(board_width, board_height, food, health, snake, enemies):
    """Return next best move for the given snake."""
    board = Board(board_width, board_height, food, snake, enemies)
    snake = Snake(snake)

    pellet = board.get_closest_pellet(snake.get_head())
    distance_to_food = snake.get_distance_from(board, pellet)
    safe_moves = snake.get_moves_safe(board)

    buff = 10

    best_moves = []
    if health < distance_to_food + buff:
        best_moves = snake.get_moves_to(board, pellet)
    else:
        best_moves = snake.get_moves_to_tail(board)

    moves = list(set(safe_moves) & set(best_moves))
    move = Directions.UP
    if moves:
        move = moves[0]
    elif safe_moves:
        move = safe_moves[0]

    return move
