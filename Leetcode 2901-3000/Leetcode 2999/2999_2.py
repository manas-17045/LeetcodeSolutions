# Leetcode 2999: Count the Number of Powerful Integers
# https://leetcode.com/problems/count-the-number-of-powerful-integers/
# Solved on 21st of June, 2025
from functools import lru_cache


class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        """
        Counts the number of "powerful integers" within a given range [start, finish].

        A powerful integer is defined as an integer whose suffix of length `len(s)` is equal to `s`,
        and all its digits (excluding the suffix) are less than or equal to `limit`.

        Args:
            start: The inclusive range [start, finish] from where to search for powerful integers.
            finish: The inclusive range [start, finish] up until where to search.
            limit: The maximum allowed digit for the prefix of the powerful integer.
            s: The required suffix string.
        """
        # Length of the suffix
        k = len(s)
        m = 10 ** k
        rem = int(s)

        # Helper function
        def ceilDiv(a: int, b: int) -> int:
            q, r = divmod(a, b)
            return q if r == 0 else (q + 1)

        lo = max(0, ceilDiv((start - rem), m))
        hi = (finish - rem) // m
        if hi < lo:
            return 0

        def countUpto(N: int) -> int:
            if N < 0:
                return 0
            sN = list(map(int, str(N)))
            L = len(sN)

            @lru_cache(None)
            def dp(pos: int, tight: bool) -> int:
                # If we've placed all digits, that's one valid number
                if pos == L:
                    return 1
                up = sN[pos] if tight else 9
                total = 0
                # Choose digit d at this position
                for d in range(0, (up + 1)):
                    if d > limit:
                        break
                    total += dp((pos + 1), tight and (d == up))
                return total

            return dp(0, True)

        return countUpto(hi) - countUpto(lo - 1)