# Leetcode 1621: Number of Sets of K Non-Overlapping Line Segments
# https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/
# Solved on 3rd of September, 2025
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        """
        Calculates the number of ways to draw k non-overlapping line segments.

        Args:
            n (int): The number of points available (from 0 to n-1).
            k (int): The number of non-overlapping line segments to draw.
        Returns:
            int: The number of sets of k non-overlapping line segments, modulo 10^9 + 7.
        """
        mod = 10**9 + 7

        nComb = n + k - 1
        kComb = 2 * k

        if kComb > nComb:
            return 0

        result = 1
        for i in range(1, (kComb + 1)):
            numerator = nComb - i + 1
            denominatorInv = pow(i, mod - 2, mod)

            result = (result * numerator) % mod
            result = (result * denominatorInv) % mod

        return result