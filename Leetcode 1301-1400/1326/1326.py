# Leetcode 1326: Minimum Number of Taps to Open to Water a Garden
# https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/
# Solved o 30th of November, 2025
class Solution:
    def minTaps(self, n: int, ranges: list[int]) -> int:
        """
        Calculates the minimum number of taps to open to water a garden of length n.

        The garden is represented as a line segment from 0 to n.
        There are n + 1 taps located at positions 0, 1, ..., n.
        Each tap i has a range ranges[i] that can water the area [i - ranges[i], i + ranges[i]].

        Args:
            n: The length of the garden.
            ranges: A list of integers where ranges[i] is the range of tap i.

        Returns:
            The minimum number of taps to open to water the entire garden. Returns -1 if it's not possible.
        """
        maxReach = [0] * (n + 1)
        for i, r in enumerate(ranges):
            start = max(0, i - r)
            end = min(n, i + r)
            maxReach[start] = max(maxReach[start], end)

        taps = 0
        currentEnd = 0
        nextEnd = 0

        for i in range(n):
            nextEnd = max(nextEnd, maxReach[i])
            if i == currentEnd:
                if nextEnd <= i:
                    return -1
                taps += 1
                currentEnd = nextEnd

        return taps