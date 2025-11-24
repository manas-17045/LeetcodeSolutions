# Leetcode 3623: Count Number of Trapezoids I
# https://leetcode.com/problems/count-number-of-trapezoids-i/
# Solved on 24th of November, 2025
from collections import Counter


class Solution:
    def countTrapezoids(self, points: list[list[int]]) -> int:
        """
        Counts the number of trapezoids that can be formed from the given points.

        Args:
            points: A list of points, where each point is represented as [x, y].
        Returns:
            The total number of trapezoids modulo 10^9 + 7.
        """
        mod = 10 ** 9 + 7
        yFrequency = Counter()
        for point in points:
            yFrequency[point[1]] += 1

        totalTrapezoids = 0
        sumOfPairs = 0

        for count in yFrequency.values():
            if count < 2:
                continue

            currentPairs = count * (count - 1) // 2
            currentPairs %= mod

            totalTrapezoids = (totalTrapezoids + sumOfPairs * currentPairs) % mod
            sumOfPairs = (sumOfPairs + currentPairs) % mod

        return totalTrapezoids