# Leetcode 2535: Difference Between Element Sum and Digit Sum of an Array
# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/
# Solved on 5th of September, 2025
class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        """
        Calculates the absolute difference between the sum of elements and the sum of digits of all elements in a list of integers.

        Args:
            nums (list[int]): A list of integers.

        Returns:
            int: The absolute difference between the element sum and the digit sum.
        """
        # Element sum: sum of numbers
        elem_sum = 0
        # Digit sum: sum of all digits of numbers
        digit_sum = 0

        for x in nums:
            elem_sum += x
            # Add digits of x without converting to string
            while x:
                digit_sum += x % 10
                x //= 10

        return abs(elem_sum - digit_sum)