# Leetcode 3442: Maximum Difference Between Even and Odd Frequency I
# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/
# Solved on 10th of June, 2025
import collections


class Solution:
    def maxDifference(self, s: str) -> int:
        """
        Calculates the maximum difference between the maximum frequency of a character
        with an odd frequency and the minimum frequency of a character with an even frequency.

        Args:
            s: The input string.

        Returns:
            The maximum difference between the maximum odd frequency and the minimum even frequency.
        """
        charFreqs = collections.Counter(s)

        maxOdd = 0
        minEven = 101

        for freq in charFreqs.values():
            if freq % 2 == 1:
                maxOdd = max(maxOdd, freq)
            else:
                minEven = min(minEven, freq)

        return maxOdd - minEven