# Leetcode 3442: Maximum Difference Between Even and Odd Frequency I
# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/
# Solved on 10th of June, 2025
from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        """
        Calculates the maximum difference between the largest odd frequency and the smallest even frequency
        of characters in the given string.

        Args:
            s: The input string.

        Returns:
            The maximum difference between the largest odd frequency and the smallest even frequency.
        """
        # Count frequencies of each character
        freq = Counter(s)

        # Separate out odd and even (and > 0) frequencies
        odd_freqs = []
        even_freqs = []
        for f in freq.values():
            if f % 2 == 1:
                odd_freqs.append(f)
            elif f > 0:
                even_freqs.append(f)

        max_odd = max(odd_freqs)
        min_even = min(even_freqs)

        return max_odd - min_even