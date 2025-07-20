# Leetcode 3519: Count Numbers with Non-Decreasing Digits
# https://leetcode.com/problems/count-numbers-with-non-decreasing-digits
# Solved on 20th of July, 2025
from functools import lru_cache


class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        """
        Counts the number of integers in the range [l, r] (inclusive) such that their base-b representation
        has non-decreasing digits.
        :param l: A string representing the lower bound of the range.
        :param r: A string representing the upper bound of the range.
        :param b: The base for the number representation.
        :return: The count of such numbers modulo 10^9 + 7.
        """

        MOD = 10**9 + 7

        def to_base_digits(x: int):
            if x == 0:
                return [0]
            digs = []
            while x:
                digs.append(x % b)
                x //= b
            return digs[::-1]

        def count_upto(S: str) -> int:
            n = int(S)
            if n <= 0:
                return 0
            digs = to_base_digits(n)
            m = len(digs)

            @lru_cache(None)
            def dfs(pos: int, last: int, tight: bool, started: bool) -> int:
                if pos == m:
                    return 1 if started else 0

                limit = digs[pos] if tight else b - 1
                res = 0
                for d in range(limit + 1):
                    nTight = tight and (d == limit)
                    if not started:
                        # Still skipping leading zeros
                        if d == 0:
                            # Stay un-started
                            res += dfs((pos + 1), 0, nTight, False)
                        else:
                            # First non-zero digit => always ok
                            res += dfs((pos + 1), d, nTight, True)
                    else:
                        # Already started: enforce non-decreasing
                        if d >= last:
                            res += dfs((pos + 1), d, nTight, True)
                return res % MOD

            return dfs(0, 0, True, False)

        L_val = int(l)
        Lm1 = str(L_val - 1) if L_val > 0 else "0"
        ans = (count_upto(r) - count_upto(Lm1)) % MOD
        return ans