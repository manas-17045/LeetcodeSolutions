# Leetcode 3791: Number of Balanced Integers in a Range
# https://leetcode.com/problems/number-of-balanced-integers-in-a-range/
# Solved on 8th of January, 2026
from functools import lru_cache


class Solution:
    def countBalanced(self, low: int, high: int) -> int:
        """
        Counts the number of balanced integers within a given range [low, high].
        A balanced integer is one where the alternating sum of its digits is zero.

        Args:
            low (int): The lower bound of the range (inclusive).
            high (int): The upper bound of the range (inclusive).
        Returns:
            int: The total count of balanced integers in the range.
        """
        def solve(numStr):
            n = len(numStr)

            @lru_cache(None)
            def dp(idx, tight, isLeading, balance, parity):
                if idx == n:
                    return 1 if not isLeading and balance == 0 else 0

                limit = int(numStr[idx]) if tight else 9
                totalCount = 0

                for digit in range(limit + 1):
                    newTight = tight and (digit == limit)

                    if isLeading:
                        if digit == 0:
                            totalCount += dp(idx + 1, newTight, True, 0, 1)
                        else:
                            totalCount += dp(idx + 1, newTight, False, digit, -1)
                    else:
                        totalCount += dp(idx + 1, newTight, False, balance + digit * parity, -parity)

                return totalCount

            return dp(0, True, True, 0, 1)

        return solve(str(high)) - solve(str(low - 1))
