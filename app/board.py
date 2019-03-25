from .snake import Snake

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
			board[(pellet['x'], pellet['y'])] = Board.FOOD

		for snake in ([snake] + enemies):
			for life, body_part in enumerate(snake['body']):
				# life represents how many more turns that tile will be occupied
				# TODO: check if body parts are in the correct order.
				board[(body_part['x'], body_part['y'])] = life

		return board

	def is_empty(self, x, y, turn = 0):
		"""Determines whether given point is definitely empty and in bounds at the given turn."""
		in_bounds = 0 <= x < self._width and 0 <= y < self._height
		if not in_bounds:
			return False

		unoccupied = self._board.get((x, y)) is None or self._board[(x, y)] == Board.FOOD
		return unoccupied

	def get_closest_pellet(self, point):
		"""Get food closest to given point."""
		x = point['x']
		y = point['y']

		closest_pellet = None
		min_distance = -1
		for pellet in self._food:
			px = pellet['x']
			py = pellet['y']

			distance = abs(px - x) + abs(py - y)

			if closest_pellet is None or distance < min_distance:
				closest_pellet = pellet
				min_distance = distance

		return closest_pellet
