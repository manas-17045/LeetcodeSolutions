# Leetcode 2998: Minimum Number of Operations to Make X and Y Equal
# https://leetcode.com/problems/minimum-number-of-operations-to-make-x-and-y-equal/
# Solved on 4th of January, 2026
class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        """
        Calculates the minimum number of operations to make x equal to y.
        Operations allowed:
        1. Decrement x by 1.
        2. If x is divisible by 11, divide x by 11.
        3. If x is divisible by 5, divide x by 5.
        :param x: The starting integer.
        :param y: The target integer.
        :return: The minimum number of operations.
        """
        if x <= y:
            return y - x

        memo = {}

        def solve(val):
            if val <= y:
                return y - val
            if val in memo:
                return memo[val]

            res = val - y

            res = min(res, val % 11 + 1 + solve(val // 11))
            res = min(res, 11 - (val % 11) + 1 + solve(val // 11 + 1))

            res = min(res, val % 5 + 1 + solve(val // 5))
            res = min(res, 5 - (val % 5) + 1 + solve(val // 5 + 1))

            memo[val] = res
            return res

        return solve(x)