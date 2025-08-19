# Leetcode 2001: Number of Pairs of Interchangeable Rectangles
# https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/
# Solved on 19th of August, 2025
from math import gcd


class Solution:
    def interchangeableRectangles(self, rectangles: list[list[int]]) -> int:
        """
        Calculates the number of pairs of interchangeable rectangles.

        Args:
            rectangles (list[list[int]]): A list of rectangles, where each rectangle is [width, height].
        Returns:
            int: The number of pairs of interchangeable rectangles.
        """
        freq = {}
        for w, h in rectangles:
            g = gcd(w, h)
            key = (w // g, h // g)
            freq[key] = freq.get(key, 0) + 1

        ans = 0
        for count in freq.values():
            if count > 1:
                ans += count * (count - 1) // 2
        return ans