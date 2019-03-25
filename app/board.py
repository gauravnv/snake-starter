from .snake import Snake
from .point import Point

class Board:
	"""Represents board including food, opponent snakes, and board metadata."""

	# Constants for board spaces.
	# Positive integers are reserved for representing snakes.
	FOOD = -1

	def __init__(self, width, height, food, snake, enemies):
		self._width = width
		self._height = height
		self._food = food
		self._board = self._get_populated_board(food, snake, enemies)

	def _get_populated_board(self, food, snake, enemies):
		"""Returns dict mapping pairs of coordinates to snake parts or food."""
		board = {}

		for pellet in food:
			point = Point.from_json(pellet)
			board[point.get_coords()] = Board.FOOD

		for snake in ([snake] + enemies):
			for life, body_part in enumerate(snake['body']):
				# life represents how many more turns that tile will be occupied
				# TODO: check if body parts are in the correct order.
				point = Point.from_json(body_part)
				board[point.get_coords()] = life + 1

		return board

	def is_empty(self, point, turn = 0):
		"""Determines whether given point is definitely empty and in bounds at the given turn."""
		in_bounds = 0 <= point.x < self._width and 0 <= point.y < self._height
		if not in_bounds:
			return False

		contents = self._board.get(point.get_coords())
		return contents is None or contents == Board.FOOD

	def get_closest_pellet(self, point):
		"""Get food closest to given point."""
		closest_pellet = None
		min_distance = -1
		for pellet in self._food:
			point_pellet = Point.from_json(pellet)
			distance = Point.get_manhattan_distance(point, point_pellet)

			if closest_pellet is None or distance < min_distance:
				closest_pellet = point_pellet
				min_distance = distance

		return closest_pellet
