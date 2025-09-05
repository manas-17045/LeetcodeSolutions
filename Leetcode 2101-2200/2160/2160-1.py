# Leetcode 2160: Minimum Sum of Four Digit Number After Splitting Digits
# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/
# Solved on 5th of September, 2025
class Solution:
    def minimumSum(self, num: int) -> int:
        """
        Calculates the minimum sum of two two-digit numbers formed by splitting the digits of the input four-digit number.

        :param num: A four-digit integer.
        :return: The minimum possible sum of two two-digit numbers.
        """
        digits = sorted(str(num))
        newOne = int(digits[0] + digits[2])
        newTwo = int(digits[1] + digits[3])
        return newOne + newTwo