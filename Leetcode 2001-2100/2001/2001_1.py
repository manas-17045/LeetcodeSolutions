# Leetcode 2001: Number of Pairs of Interchangeable Rectangles
# https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/
# Solved on 19th of August, 2025
import math
from collections import defaultdict


class Solution:
    def interchangeableRectangles(self, rectangles: list[list[int]]) -> int:
        """
        Calculates the number of interchangeable pairs of rectangles.

        Args:
            rectangles: A list of lists, where each inner list [width, height] represents a rectangle.
        Returns:
            The total number of interchangeable pairs of rectangles.
        """
        ratioCounts = defaultdict(int)
        interchangeablePairs = 0

        for width, height in rectangles:
            commonDivisor = math.gcd(width, height)
            simplifiedRatio = (width // commonDivisor, height // commonDivisor)

            interchangeablePairs += ratioCounts[simplifiedRatio]
            ratioCounts[simplifiedRatio] += 1

        return interchangeablePairs