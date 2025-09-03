# Leetcode 1621: Number of Sets of K Non-Overlapping Line Segments
# https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/
# Solved on 3rd of September, 2025
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        """
        Calculates the number of ways to choose k non-overlapping line segments
        from n points on a 1D line.

        Args:
            n (int): The number of points on the line (from 0 to n-1).
            k (int): The number of non-overlapping line segments to choose.
        Returns:
            int: The number of ways to choose k non-overlapping line segments.
        """
        MOD = 10**9 + 7

        if k == 0:
            return 1
        if n < (k + 1):
            return 0

        prev = [1] * (n + 1)

        for seg in range(1, k + 1):
            pref = [0] * (n + 1)
            for i in range(1, (n + 1)):
                pref[i] = (pref[i - 1] + prev[i]) % MOD

            cur = [0] * (n + 1)
            for i in range(1, n + 1):
                cur[i] = (cur[i - 1] + pref[i - 1]) % MOD

            prev = cur

        return prev[n]