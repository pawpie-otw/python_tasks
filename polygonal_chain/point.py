from __future__ import annotations
import itertools as its


class Point:
    """Class defining a point in 2D area.
    """
    auto_id = its.count()
    __slots__ = ['x', 'y', 'id']

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
        self.id = next(__class__.auto_id)

    def distance_to_other(self, other: Point) -> float:
        """Calculate Euclidean distance between two points,
            current and other given as the arg

        Args:
            other (Point): second point

        Returns:
            float: distance from current to other point
        """
        sum_pow_diff = (self.x - other.x) ** 2 + (self.y - other.y) ** 2

        #
        return sum_pow_diff ** .5

    def __str__(self) -> str:
        """Return short description of instance as string"""

        return f"id: {self.id}, x: {self.x}, y: {self.y}"

    def __repr__(self) -> str:
        return self.__str__()
