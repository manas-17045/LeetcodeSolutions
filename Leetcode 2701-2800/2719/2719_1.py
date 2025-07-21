# Leetcode 2719: Count of Integers
# https://leetcode.com/problems/count-of-integers/
# Solved on 20th of July, 2025
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        """
        Counts the number of integers x such that num1 <= x <= num2 and the sum of digits of x is between min_sum and max_sum (inclusive).
        :param num1: A string representing the lower bound of the range.
        :param num2: A string representing the upper bound of the range.
        :param min_sum: The minimum allowed sum of digits.
        :param max_sum: The maximum allowed sum of digits.
        :return: The count of such integers modulo 10^9 + 7.
        """
        MOD = 10**9 + 7

        def getCount(s: str) -> int:
            memo = {}
            n = len(s)

            def solve(index: int, currentSum: int, isTight: bool) -> int:
                if currentSum > max_sum:
                    return 0

                if index == n:
                    return 1 if currentSum >= min_sum else 0

                state = (index, currentSum, isTight)
                if state in memo:
                    return memo[state]

                ans = 0
                upperBound = int(s[index]) if isTight else 9

                for digit in range(upperBound + 1):
                    newIsTight = isTight and (digit == upperBound)
                    ans = (ans + solve(index + 1, currentSum + digit, newIsTight)) % MOD

                memo[state] = ans
                return ans

            return solve(0, 0, True)

        def subtractOne(s: str) -> str:
            return str(int(s) - 1)

        num1MinusOne = subtractOne(num1)

        countToNum2 = getCount(num2)
        countToNum1MinusOne = getCount(num1MinusOne)

        result = (countToNum2 - countToNum1MinusOne + MOD) % MOD
        return result