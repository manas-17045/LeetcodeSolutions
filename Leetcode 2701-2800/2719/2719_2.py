# Leetcode 2719: Count of Integers
# https://leetcode.com/problems/count-of-integers/
# Solved on 20th of July, 2025
from functools import lru_cache


class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        """
        Counts the number of integers x such that num1 <= x <= num2 and min_sum <= sum_of_digits(x) <= max_sum.
        :param num1: The lower bound of the range (inclusive), as a string.
        :param num2: The upper bound of the range (inclusive), as a string.
        :param min_sum: The minimum allowed sum of digits.
        :param max_sum: The maximum allowed sum of digits.
        :return: The count of such integers modulo 10^9 + 7.
        """
        MOD = 10**9 + 7

        def dec_str(s: str) -> str:
            if s == "0":
                return "0"
            a = list(s)
            i = len(a) - 1
            while i >= 0:
                if a[i] == '0':
                    a[i] = '9'
                    i -= 1
                else:
                    a[i] = str(int(a[i]) - 1)
                    break

            res = ''.join(a).lstrip('0')
            return res if res else "0"

        def count_upto(bound: str) -> int:
            n = len(bound)

            @lru_cache(None)
            def dp(pos: int, tight: bool, digit_sum: int) -> int:
                if digit_sum > max_sum:
                    return 0

                if pos == n:
                    return 1 if min_sum <= digit_sum <= max_sum else 0

                res = 0
                up = int(bound[pos]) if tight else 9
                for dig in range(0, (up + 1)):
                    nTight = tight and (dig == up)
                    res = (res + dp(pos + 1, nTight, digit_sum + dig)) % MOD

                return res

            return dp(0, True, 0)

        low = dec_str(num1)
        ans = count_upto(num2) - count_upto(low)
        return ans % MOD