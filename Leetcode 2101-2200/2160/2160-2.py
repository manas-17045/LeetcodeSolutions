# Leetcode 2160: Minimum Sum of Four Digit Number After Splitting Digits
# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/
# Solved on 5th of September, 2025
class Solution:
    def minimumSum(self, num: int) -> int:
        """
        Calculates the minimum possible sum of two new numbers formed by
        splitting the digits of the input number.

        Args:
            num (int): A 4-digit positive integer.
        Returns:
            int: The minimum sum of the two new numbers.
        """
        # Extract digits (thousands, hundreds, tens, ones)
        d0 = num // 1000
        d1 = (num // 100) % 10
        d2 = (num // 10) % 10
        d3 = num % 10

        digits = [d0, d1, d2, d3]
        digits.sort()

        # To minimize the sum, use the two smallest digits as the tens digits
        # of the two numbers and the remaining digits as the ones digits.
        new1 = digits[0] * 10 + digits[2]
        new2 = digits[1] * 10 + digits[3]
        return new1 + new2