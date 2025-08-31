# Leetcode 1664: Ways to Make a Fair Array
# https://leetcode.com/problems/ways-to-make-a-fair-array/
# Solved on 31st of August, 2025
class Solution:
    def waysToMakeFair(self, nums: list[int]) -> int:
        """
        Calculates the number of ways to make an array "fair" by removing one element.
        An array is fair if the sum of its even-indexed elements equals the sum of its odd-indexed elements.

        Args:
            nums: A list of integers.
        Returns:
            The number of indices such that if the element at that index is removed, the remaining array is fair.
        """
        rightEvenSum = sum(nums[::2])
        rightOddSum = sum(nums[1::2])

        leftEvenSum = 0
        leftOddSum = 0
        count = 0

        for i, currentNum in enumerate(nums):
            if i % 2 == 0:
                rightEvenSum -= currentNum
            else:
                rightOddSum -= currentNum

            if leftEvenSum + rightOddSum == leftOddSum + rightEvenSum:
                count += 1

            if i % 2 == 0:
                leftEvenSum += currentNum
            else:
                leftOddSum += currentNum

        return count