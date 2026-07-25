# Leetcode 3536: Maximum Product of Two Digits
# https://leetcode.com/problems/maximum-product-of-two-digits/
# Solved on 25th of July, 2026
class Solution:
    def maxProduct(self, n: int) -> int:
        """
        Finds the maximum product of two distinct digits of a given integer.
        @param n: The integer to find the maximum product of two digits.
        @return: The maximum product of two distinct digits.
        """
        firstMax = 0
        secondMax = 0

        while n > 0:
            currentDigit = n % 10
            if currentDigit > firstMax:
                secondMax = firstMax
                firstMax = currentDigit
            elif currentDigit > secondMax:
                secondMax = currentDigit
            n //= 10
        
        return firstMax * secondMax