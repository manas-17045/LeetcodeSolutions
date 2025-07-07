# Leetcode 2318: Number of Distinct Roll Sequences
# https://leetcode.com/problems/number-of-distinct-roll-sequences/
# Solved on 7th of July, 2025
import math


class Solution:
    def distinctSequences(self, n: int) -> int:
        """
        Calculates the number of distinct roll sequences of length 'n'
        such that for any two adjacent elements in the sequence, say x and y,
        x != y and gcd(x, y) == 1. Also, for any three adjacent elements
        x, y, z, x != z.

        Args:
            n (int): The length of the roll sequence.

        Returns:
            int: The number of distinct roll sequences modulo 10^9 + 7.
        """
        memo = {}
        mod = 10**9 + 7

        def solve(index, p1, p2):
            if index == n:
                return 1

            state = (index, p1, p2)
            if state in memo:
                return memo[state]

            ans = 0
            for roll in range(1, 7):
                if roll != p1 and roll != p2:
                    isCoprime = (p1 == 0 or math.gcd(roll, p1) == 1)
                    if isCoprime:
                        ans = (ans + solve(index + 1, roll, p1)) % mod

            memo[state] = ans
            return ans

        return solve(0, 0, 0)