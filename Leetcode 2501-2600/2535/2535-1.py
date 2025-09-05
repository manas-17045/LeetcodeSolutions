# Leetcode 2535: Difference Between Element Sum and Digit Sum of an Array
# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/
# Solved on 5th of September, 2025
class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        """
        Calculates the absolute difference between the sum of all elements in the array
        and the sum of all digits present in the array's elements.

        Args:
            nums: A list of integers.
        Returns:
            The absolute difference between the element sum and the digit sum.
        """
        elementSum = 0
        digitSum = 0
        for num in nums:
            elementSum += num

            currentNum = num
            while currentNum > 0:
                digitSum += currentNum % 10
                currentNum //= 10

        return abs(elementSum - digitSum)