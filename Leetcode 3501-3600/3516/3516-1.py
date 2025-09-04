# Leetcode 3516: Find Closest Person
# https://leetcode.com/problems/find-closest-person/
# Solved on 4th of September, 2025
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        """
        Finds which of two persons (at positions x and y) is closer to a third person (at position z).
        :param x: Position of the first person.
        :param y: Position of the second person.
        :param z: Position of the third person.
        :return: 1 if the first person is closer, 2 if the second person is closer, 0 if they are equidistant.
        """
        distPersonOne = abs(x - z)
        distPersonTwo = abs(y - z)

        return 1 if distPersonOne < distPersonTwo else 2 if distPersonTwo < distPersonOne else 0