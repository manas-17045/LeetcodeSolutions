# Leetcode 3959: Check Good Integer
# https://leetcode.com/problems/check-good-integer/
# Solved on 29th of June, 2026
class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        """
        Checks if the given integer is a good integer.
        A good integer is an integer that contains at least three consecutive occurrences of the same digit.
        @param n: The integer to check.
        @return: True if the integer is a good integer, False otherwise.
        """
        totalDiff = 0

        while n > 0:
            currentDigit = n % 10
            totalDiff += currentDigit * (currentDigit - 1)
            if totalDiff >= 50:
                return True

            n //= 10

        return False