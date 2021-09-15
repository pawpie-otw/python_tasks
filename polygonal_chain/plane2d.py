from typing import List, Tuple
from point import Point
import numpy as np
from random import randint


class Plane2D:

    def __init__(self, points: List[Point]) -> None:
        self.points = points

    def polygonal_chain(self) -> Tuple[List[int], float]:
        """Draw a random point from list of points and seek
        next points, which are the nearest to the previous one connecting these
        points in polygonal chain.
        Then return list of consecutive ids of points and len of this chain.

        Returns:
            Tuple[List[int], float]: list of ids, len of polygonal chain
        """
        # initialize containers and prepare data
        copied_points = self.points.copy()
        pol_chain_order = []
        distance = 0

        # draw random point
        cur_point = copied_points.pop(randint(0, len(copied_points)-1))

        # adding above point as the first one
        pol_chain_order.append(cur_point.id)

        while copied_points:
            # find id and distance of the nearest point
            next_id, distance_i = self._find_nearest_point(
                cur_point, copied_points)

            # update data with above results
            distance += distance_i
            cur_point = copied_points.pop(next_id)
            pol_chain_order.append(cur_point.id)

        # return ordered points by id list and total sum of distances
        return pol_chain_order, distance

    def _find_nearest_point(self, point_a: Point,
                           points_list: List[Point]) -> Tuple[int, float]:
        """Calculate distance from start point to the nearest one

        Args:
            point_a (Point): starting point
            points_list (List[Point]): list of points to find nearest

        Returns:
            Tuple[int, float]: id, distance to nearest point
        """

        # calculate distance to every point in current plane
        distances = np.array([point_a.distance_to_other(point_b)
                              for point_b in points_list])

        # return id, distance to nearest point
        return np.argmin(distances), np.amin(distances)


if __name__ == '__main__':
    plane2d = Plane2D([Point(i*2-5, (i+1) * .3)
                       for i in range(10)])

    print(plane2d.polygonal_chain())
