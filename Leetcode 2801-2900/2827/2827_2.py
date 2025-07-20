# Leetcode 2827: Number of Beautiful Integers in the Range
# https://leetcode.com/problems/number-of-beautiful-integers-in-the-range/
# Solved on 20th of July, 2025
from functools import lru_cache


class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        """
        Calculates the number of "beautiful" integers within a given range [low, high].
        A beautiful integer is defined as a number where the count of even digits equals the count of odd digits,
        and the number is divisible by k.
        :param low: The lower bound of the range (inclusive).
        :param high: The upper bound of the range (inclusive).
        :param k: The divisor for the beautiful integers.
        :return: The total count of beautiful integers in the range [low, high].
        """
        def count_up_to(n: int) -> int:
            s = str(n)
            L = len(s)

            @lru_cache(None)
            def dp(pos: int, diff: int, mod: int, tight: bool, started: bool) -> int:
                if pos == L:
                    return int(started and diff == 0 and mod == 0)

                total = 0
                max_d = int(s[pos]) if tight else 9

                for d in range(max_d + 1):
                    nTight = tight and (d == max_d)
                    if not started and d == 0:
                        total += dp(pos + 1, 0, 0, nTight, False)
                    else:
                        nDiff = diff + (1 if d % 2 == 0 else -1)
                        nMod = (mod * 10 + d) % k
                        total += dp(pos + 1, nDiff, nMod, nTight, True)

                return total

            return dp(0, 0, 0, True, False)

        return count_up_to(high) - count_up_to(low - 1)