import json
from bottle import HTTPResponse

from .constants import Directions

def ping_response():
    return HTTPResponse(
        status=200
    )

def start_response(color):
    assert type(color) is str, \
        "Color value must be string"

    return HTTPResponse(
        status=200,
        headers={
            "Content-Type": "application/json"
        },
        body=json.dumps({
            "color": color,
            "headType": "fang",
            "tailType": "bolt"
        })
    )

def move_response(move):
    assert move in [Directions.UP, Directions.DOWN, Directions.LEFT, Directions.RIGHT], \
        "Move must be one of [up, down, left, right]"

    return HTTPResponse(
        status=200,
        headers={
            "Content-Type": "application/json"
        },
        body=json.dumps({
            "move": move
        })
    )

def end_response():
    return HTTPResponse(
        status=200
    )
