import bottle
import json
import random

from .middleware import *
from .board import Board

from .api import start_response, move_response, end_response

game_board = None
