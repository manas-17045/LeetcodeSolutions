# Leetcode 1515: Best Position for a Service Centre
# https://leetcode.com/problems/best-position-for-a-service-centre/
# Solved on 9th of September, 2025
import math


class Solution:
    def getMinDistSum(self, positions: list[list[int]]) -> float:
        """
        Calculates the minimum sum of Euclidean distances from a point to all given points.

        :param positions: A list of lists, where each inner list represents a point [x, y].
        :return: The minimum sum of distances as a float.
        """
        def total_dist(x: float, y: float) -> float:
            s = 0.0
            for px, py in positions:
                s += math.hypot(x - px, y - py)
            return s

        n = len(positions)
        if n == 0:
            return 0.0
        x = sum(p[0] for p in positions) / n
        y = sum(p[1] for p in positions) / n

        eps = 1e-7
        dist_eps = 1e-12
        max_iter = 10000

        for _ in range(max_iter):
            num_x = 0.0
            num_y = 0.0
            den = 0.0
            for px, py in positions:
                d = math.hypot(x - px, y - py)
                if d < dist_eps:
                    return total_dist(px, py)
                w = 1.0 / d
                num_x += px * w
                num_y += py * w
                den += w

            new_x = num_x / den
            new_y = num_y / den

            if math.hypot(new_x - x, new_y - y) < eps:
                x, y = new_x, new_y
                break
            x, y = new_x, new_y

        return total_dist(x, y)