# Leetcode 3516: Find Closest Person
# https://leetcode.com/problems/find-closest-person/
# Solved on 4th of September, 2025
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        """
        Finds which of x or y is closer to z.
        :param x: An integer.
        :param y: An integer.
        :param z: An integer.
        :return: 1 if x is closer to z, 2 if y is closer to z, and 0 if they are equidistant.
        """
        dx = abs(x - z)
        dy = abs(y - z)

        if dx < dy:
            return 1

        if dy < dx:
            return 2

        return 0