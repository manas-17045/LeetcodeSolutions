# Leetcode 3723: Maximize Sum of Squares of Digits
# https://leetcode.com/problems/maximize-sum-of-squares-of-digits/
# Solved on 21st of November, 2025
class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        """
        Maximizes the sum of squares of digits for a given number of digits and a target sum.
        :param num: The number of digits in the resulting string.
        :param sum: The target sum of the digits.
        :return: A string representing the number with the maximized sum of squares of digits,
                 or an empty string if no such number exists.
        """
        if sum > 9 * num:
            return ""

        ninesCount = sum // 9
        remainder = sum % 9

        if ninesCount == num:
            return "9" * num

        zerosCount = num - ninesCount - 1
        return "9" * ninesCount + str(remainder) + "0" * zerosCount