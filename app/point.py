
class Point:
    """Represents two dimensional coordinates."""

    def __init__(self, data):
        self._x = data['x']
        self._y = data['y']

    @staticmethod
    def get_manhattan_distance(point1, point2):
        return abs(point1._x - point2._x) + abs(point1._y - point2._y)

    def copy(self, dx = 0, dy = 0):
        data = {
            'x': self._x + dx,
            'y': self._y + dy
        }
        return Point(data)
