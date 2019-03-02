import os
import bottle
import copy
import json
import random
import math

from .game_handlers import *
from .AStar import *
from .api import ping_response
from .middleware import *
from .api import start_response, move_response, end_response

snake = None
board = None
SNAKE = 1
WALL = 2
FOOD = 3
BUFFER = 3
CHILL = 4
ID = 0


def distance(p, q):
    dx = abs(p[0] - q[0])
    dy = abs(p[1] - q[1])
    return dx + dy

def init(food, snakes, height, width, ID):
    
    board = [[0 for col in range(height)] for row in range(width)]

    for snake in snakes:
        if snake['id']== ID:
            mysnake = snake
        for coord in snake['body']:
            board[coord['x']][coord['y']] = SNAKE

    for x in range(width-1, width):
        for y in range(height-1, height):
            board[x][y] = WALL

    for f in food:
        board[f['x']][f['y']] = FOOD

    return mysnake, board


@bottle.post('/start')
def start():
    data = bottle.request.json

    height = int(data["board"]["height"])
    width = int(data["board"]["width"])
    turn = int(data["turn"])
    health = int(data["you"]["health"])
    myBody = data["board"]["snakes"][0]["body"]
    food = list(data["board"]["food"])
    snakes = list(data["board"]["snakes"])

    global game_board
    game_board = Board(width, height)
    game_board.update(food, snakes)

    color = "#011f4b"

    return start_response(color)

@bottle.post('/move')
@timer
def move():
    data = bottle.request.json
    height = int(data["board"]["height"])
    width = int(data["board"]["width"])
    turn = int(data["turn"])
    health = int(data["you"]["health"])
    myBody = data["board"]["snakes"][0]["body"]
    food = list(data["board"]["food"])
    snakes = list(data["board"]["snakes"])
    ID = str(data["you"]["id"])

    snake, board = init(food, snakes, height, width, ID)


    for enemy in snakes:
        if (enemy['id'] == ID):
            continue
        if distance(snake['coords'][0], enemy['coords'][0]) > BUFFER:
            continue
        if (len(enemy['coords']) > len(snake['coords'])-1):
            #dodge
            if enemy['body']['x']['y'] < height-1:
                board[enemy['body']['x']['x']][enemy['body']['x']['y']+1] = CHILL
            if enemy['body']['x']['y'] > 0:
                board[enemy['body']['x']['x']][enemy['body']['x']['y']-1] = CHILL

            if enemy['body']['x']['x'] < width-1:
                board[enemy['body']['x']['x']+1][enemy['body']['x']['y']] = CHILL
            if enemy['body']['x']['x'] > 0:
                board[enemy['body']['x']['x']-1][enemy['body']['x']['y']] = CHILL

    snake_head = snake['body'][0]
    snake_body = snake['body']
    path = None

    middle = [width / 2, height / 2]
    foods = sorted(food, key = lambda p: distance(p,middle))
    
    for food in foods:
        #print food
        tentative_path = a_star(snek_head, food, grid, snek_coords)
        if not tentative_path:
            #print "no path to food"
            continue

        path_length = len(tentative_path)
        snek_length = len(snek_coords) + 1

        dead = False
        for enemy in data['snakes']:
            if enemy['id'] == ID:
                continue
            if path_length > distance(enemy['coords'][0], food):
                dead = True
        if dead:
            continue

        # Update snek
        if path_length < snek_length:
            remainder = snek_length - path_length
            new_snek_coords = list(reversed(tentative_path)) + snek_coords[:remainder]
        else:
            new_snek_coords = list(reversed(tentative_path))[:snek_length]

        if grid[new_snek_coords[0][0]][new_snek_coords[0][1]] == FOOD:
            # we ate food so we grow
            new_snek_coords.append(new_snek_coords[-1])

        # Create a new grid with the updates snek positions
        new_grid = copy.deepcopy(grid)

        for coord in snek_coords:
            new_grid[coord[0]][coord[1]] = 0
        for coord in new_snek_coords:
            new_grid[coord[0]][coord[1]] = SNAKE

        #printg(grid, 'orig')
        #printg(new_grid, 'new')

        #print snek['coords'][-1]
        foodtotail = a_star(food,new_snek_coords[-1],new_grid, new_snek_coords)
        if foodtotail:
            path = tentative_path
            break
        #print "no path to tail from food"



    if not path:
        path = a_star(snek_head, snek['coords'][-1], grid, snek_coords)

    despair = not (path and len(path) > 1)

    if despair:
        for neighbour in neighbours(snek_head,grid,0,snek_coords, [1,2,5]):
            path = a_star(snek_head, neighbour, grid, snek_coords)
            #print 'i\'m scared'
            break

    despair = not (path and len(path) > 1)


    if despair:
        for neighbour in neighbours(snek_head,grid,0,snek_coords, [1,2]):
            path = a_star(snek_head, neighbour, grid, snek_coords)
            #print 'lik so scared'
            break

    if path:
        assert path[0] == tuple(snek_head)
        assert len(path) > 1

    return {
        'move': direction(path[0], path[1]),
        'taunt': 'TRAITOR!'
    }
   

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
    myBody = data["board"]["snakes"][0]["body"]
    food = list(data["board"]["food"])
    snakes = list(data["board"]["snakes"])

    """
    TODO: If your snake AI was stateful,
        clean up any stateful objects here.
    """
    print(json.dumps(data))

    return end_response()

@bottle.route('/')
def index():
    return '''
    Battlesnake documentation can be found at
       <a href="https://docs.battlesnake.io">https://docs.battlesnake.io</a>.
    '''

@bottle.route('/static/<path:path>')
def static(path):
    """
    Given a path, return the static file located relative
    to the static folder.

    This can be used to return the snake head URL in an API response.
    """
    return bottle.static_file(path, root='static/')

@bottle.post('/ping')
def ping():
    """
    A keep-alive endpoint used to prevent cloud application platforms,
    such as Heroku, from sleeping the application instance.
    """
    return ping_response()

# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()

def main():
    bottle.run(
        application,
        host=os.getenv('IP', '0.0.0.0'),
        port=os.getenv('PORT', '8080'),
        debug=os.getenv('DEBUG', True)
    )

if __name__ == '__main__':
    main()
