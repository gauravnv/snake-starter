
class Board:
	"""Represents board including food, opponent snakes, and board metadata."""

	# Constants for board spaces.
	# Positive integers are reserved for representing snakes.
	FOOD = -1
	EMPTY = -2

	def __init__(self, width, height):
		self.width = width
		self.height = height

		self.food = []
		self.snakes = []

		self.board = []
		for i in range(width):
			self.board.append([])
			for j in range(height):
				self.board[i].append(Board.EMPTY)

	def update(self, food, snakes):
		"""Updates food and opponent snake positions on board."""
		self.food = food
		self.snakes = snakes

		for pellet in food:
			self.board[pellet['x']][pellet['y']] == Board.FOOD

		for snake in snakes:
			for life, body_part in enumerate(snake['body']):
				# life represents how many more turns that tile will be occupied
				# TODO: check if body parts are in the correct order.
				self.board[body_part['x']][body_part['y']] == life

		self.food = food
		self.snakes = snakes

	def is_empty(self, x, y, turn = 0):
		"""Determines whether given point is definitely empty and in bounds at the given turn."""
		in_bounds = 0 <= x < self.width and 0 <= y < self.height
		if not in_bounds:
			return False

		unoccupied = self.board[x][y] < 0
		return unoccupied
