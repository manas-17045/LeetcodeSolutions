# Leetcode 2801: Count Stepping Numbers in Range
# https://leetcode.com/problems/count-stepping-numbers-in-range/
# Solved on 15th of September, 2025
from functools import lru_cache


class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        """
        Counts the number of stepping numbers in the range [low, high].
        A stepping number is a number where the absolute difference between adjacent digits is 1.
        :param low: The lower bound of the range as a string.
        :param high: The upper bound of the range as a string.
        :return: The count of stepping numbers in the given range modulo 10^9 + 7.
        """
        MOD = 10**9 + 7

        def dec_str(s: str) -> str:
            # Subtract 1 from decimal string s
            if s == "0":
                return "-1"
            arr = list(s)
            i = len(arr) - 1
            while i >= 0:
                if arr[i] == "0":
                    arr[i] = "9"
                    i -= 1
                else:
                    arr[i] = chr(ord(arr[i]) - 1)
                    break

            # Remove any leading zeros (shouldn't produce any except possibly if input was "1")
            res = ''.join(arr).lstrip('0')
            return res if res != '' else '0'

        def count_leq(bound: str) -> int:
            # If bound is negative string like "-1"
            if bound.startswith('-'):
                return 0
            digits = list(map(int, bound))
            n = len(digits)

            @lru_cache(None)
            def dfs(pos: int, prev: int, tight: int, started: int) -> int:
                if pos == n:
                    return 1

                res = 0
                up = digits[pos] if tight else 9
                for d in range(0, (up + 1)):
                    nTight = 1 if (tight and d == up) else 0
                    if not started:
                        if d == 0:
                            # Still not started; leading zeros continue
                            res += dfs(pos + 1, -1, nTight, 0)
                        else:
                            # First non-zero digit, no adjacency constraint
                            res += dfs(pos + 1, d, nTight, 1)
                    else:
                        # Already started: must satisfy |prev- d| == 1
                        if abs(prev - d) == 1:
                            res += dfs(pos + 1, d, nTight, 1)
                        else:
                            # Not allowed
                            continue

                return res % MOD

            return dfs(0, -1, 1, 0) % MOD

        low_minus_one = dec_str(low)
        ans = (count_leq(high) - count_leq(low_minus_one)) % MOD
        return ans