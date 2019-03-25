import bottle
import json
import random

from .middleware import *
from .game_logic import get_next_move

from .api import start_response, move_response, end_response

@bottle.post('/start')
def start():
    color = "#011f4b"
    return start_response(color)

@bottle.post('/move')
@timer
def move():
    data = bottle.request.json

    # Extract data from JSON.
    width = data["board"]["width"]
    height = data["board"]["height"]
    health = data["you"]["health"]
    food = data["board"]["food"]
    player = data["you"]
    snakes = data["board"]["snakes"]

    move = get_next_move(width, height, food, player, snakes)

    return move_response(move)

@bottle.post('/end')
def end():
    return end_response()
