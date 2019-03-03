import bottle
import json
import random

from .middleware import *
from .board import Board

from .api import start_response, move_response, end_response

game_board = None

@bottle.post('/start')
def start():
    data = bottle.request.json

    height = int(data["board"]["height"])
    width = int(data["board"]["width"])
    turn = int(data["turn"])
    health = int(data["you"]["health"])
    myBody = data["board"]["snakes"][0]["body"]

    food = data["board"]["food"]
    snakes = data["board"]["snakes"]
    you = data["you"]

    global game_board
    game_board = Board(width, height, food, snakes, you)

    """
    TODO: If you intend to have a stateful snake AI,
            initialize your snake state here using the
            request's data if necessary.
    """
    print(json.dumps(data))

    color = "#011f4b"

    return start_response(color)

@bottle.post('/move')
@timer
def move():
    data = bottle.request.json

    turn = int(data["turn"])
    health = int(data["you"]["health"])

    food = data["board"]["food"]
    snakes = data["board"]["snakes"]
    you = data["you"]

    game_board.update(food, snakes, you)

    """
    TODO: Using the data from the endpoint request object, your
            snake AI must choose a direction to move in.
    """
    print(json.dumps(data))

    food_directions = game_board.get_directions_closest_pellet()
    possible_directions = game_board.get_possible_moves()

    moves = list(set(food_directions) & set(possible_directions))
    move = 'up'
    if moves:
        move = random.choice(moves)
    elif possible_directions:
        move = random.choice(possible_directions)

    return move_response(move)

@bottle.post('/end')
def end():
    data = bottle.request.json

    height = int(data["board"]["height"])
    width = int(data["board"]["width"])
    turn = int(data["turn"])
    health = int(data["you"]["health"])
    food = list(data["board"]["food"])
    snakes = list(data["board"]["snakes"])

    """
    TODO: If your snake AI was stateful,
        clean up any stateful objects here.
    """
    print(json.dumps(data))

    return end_response()
