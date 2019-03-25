
class Point:
    """Represents two dimensional coordinates."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # TODO: correct decorator.
    @staticmethod
    def from_json(data):
        x = data['x']
        y = data['y']

        return Point(x, y)

    @staticmethod
    def get_manhattan_distance(point1, point2):
        return abs(point1.x - point2.x) + abs(point1.y - point2.y)

    def get_coords(self):
        return (self.x, self.y)

    def copy(self, dx = 0, dy = 0):
        return Point(self.x + dx, self.y + dy)
