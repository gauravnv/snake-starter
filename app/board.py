from .snake import Snake

class Board:
	"""Represents board including food, opponent snakes, and board metadata."""

	# Constants for board spaces.
	# Positive integers are reserved for representing snakes.
	FOOD = -1

	def __init__(self, width, height, food, snakes, player):
		self.width = width
		self.height = height

		self.food = []
		self.enemy_snakes = {}
		self.player_snake = None

		self._board = {}

		self.update(food, snakes, player)

	def update(self, food, snakes, player):
		"""Updates food and opponent snake positions on board."""
		self._board = {}

		self.food = food
		for snake in snakes:
			self.enemy_snakes[snake['id']] = Snake(snake)

		self.player_snake = Snake(player)

		for pellet in food:
			self._board[(pellet['x'], pellet['y'])] = Board.FOOD

		for snake in snakes:
			for life, body_part in enumerate(snake['body']):
				# life represents how many more turns that tile will be occupied
				# TODO: check if body parts are in the correct order.
				self._board[(body_part['x'], body_part['y'])] = life

	def is_empty(self, x, y, turn = 0):
		"""Determines whether given point is definitely empty and in bounds at the given turn."""
		in_bounds = 0 <= x < self.width and 0 <= y < self.height
		if not in_bounds:
			return False

		unoccupied = self._board.get((x, y)) is None or self._board[(x, y)] == Board.FOOD
		return unoccupied

	def get_possible_moves(self):
		"""Return list of possible moves for player snake."""
		return self.player_snake.get_possible_moves(self)