# Leetcode 1955: Count Number of Special Subsequences
# https://leetcode.com/problems/count-number-of-special-subsequences/
# Solved on 24th of July, 2025
class Solution:
    def countSpecialSubsequences(self, nums: list[int]) -> int:

        """
        Counts the number of special subsequences in the given list of integers.
        A special subsequence is defined as a subsequence that consists of 0s, followed by 1s, followed by 2s.

        Args:
            nums: A list of integers, where each integer is 0, 1, or 2.
        Returns:
            The number of special subsequences modulo 10^9 + 7.
        """
        MOD = 10**9 + 7
        c0 = c1 = c2 = 0

        for x in nums:
            if x == 0:
                c0 = (2 * c0 + 1) % MOD
            elif x == 1:
                c1 = (2 * c1 + c0) % MOD
            elif x == 2:
                c2 = (2 * c2 + c1) % MOD

        return c2