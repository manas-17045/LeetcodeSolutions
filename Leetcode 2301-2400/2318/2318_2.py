# Leetcode 2318: Number of Distinct Roll Sequences
# https://leetcode.com/problems/number-of-distinct-roll-sequences/
# Solved on 7th of July, 2025
import math


class Solution:
    def distinctSequences(self, n: int) -> int:
        """
        Calculates the number of distinct sequences of length n satisfying specific conditions.

        A sequence consists of integers from 1 to 6. The conditions are:
        1. Adjacent elements must be different.
        2. Adjacent elements must be coprime (their greatest common divisor is 1).
        3. The first and third elements (if they exist) must be different.

        Args:
            n: The desired length of the sequences.

        Returns:
            The number of distinct sequences modulo 10^7 + 9.
        """
        MOD = 10**7 + 9

        dp = [[0] * 7 for _ in range(7)]
        dp[0][0] = 1

        for _ in range(n):
            new_dp = [[0] * 7 for _ in range(7)]
            for prev2 in range(7):
                for prev1 in range(7):
                    if dp[prev2][prev1] == 0:
                        continue
                    ways = dp[prev2][prev1]
                    for c in range(1, 7):
                        if c == prev1:
                            continue
                        if c == prev2:
                            continue
                        if prev1 != 0 and math.gcd(prev1, prev2) != 1:
                            continue
                        new_dp[prev1][c] = (new_dp[prev1][c] + ways) % MOD
            dp = new_dp

        # Sum over all ending pairs
        return sum(dp[i][j] for i in range(7) for j in range(7)) % MOD