import bottle
import json
import random
import middleware

from .api import start_response, move_response, end_response

board = None

@bottle.post('/start')
def start():
    data = bottle.request.json

    height = int(data["board"]["height"])
    width = int(data["board"]["width"])
    turn = int(data["turn"])
    health = int(data["you"]["health"])
    myBody = {
        'x': 0,
        'y': 0
    }
    food = list(data["board"]["food"])
    snakes = list(data["board"]["snakes"])    

    """
    TODO: If you intend to have a stateful snake AI,
            initialize your snake state here using the
            request's data if necessary.
    """
    print(json.dumps(data))

    color = "#00FF00"

    return start_response(color)

@bottle.post('/move')
@middleware.timer
def move():
    data = bottle.request.json
    height = int(data["board"]["height"])
    width = int(data["board"]["width"])
    turn = int(data["turn"])
    health = int(data["you"]["health"])
    myBody = {
        'x': 0,
        'y': 0
    }
    food = list(data["board"]["food"])
    snakes = list(data["board"]["snakes"])

    """
    TODO: Using the data from the endpoint request object, your
            snake AI must choose a direction to move in.
    """
    print(json.dumps(data))
    # print("food: ")
    # print(food)
    # print("snakes: ") 
    # print(snakes)
    # print("body coords:")
    # print(myBody)
    # print("health: " + str(health))
    # print("width: " + str(width))

    directions = ['up', 'down', 'left', 'right']
    direction = random.choice(directions)

    return move_response(direction)

@bottle.post('/end')
def end():
    data = bottle.request.json

    height = int(data["board"]["height"])
    width = int(data["board"]["width"])
    turn = int(data["turn"])
    health = int(data["you"]["health"])
    myBody = {
        'x': 0,
        'y': 0
    }
    food = list(data["board"]["food"])
    snakes = list(data["board"]["snakes"])

    """
    TODO: If your snake AI was stateful,
        clean up any stateful objects here.
    """
    print(json.dumps(data))

    return end_response()
