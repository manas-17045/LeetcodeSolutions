# Leetcode 2221: Find Triangular Sum of an Array
# https://leetcode.com/problems/find-triangular-sum-of-an-array/
# Solved on 9th of September, 2025
class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        """
        Calculates the triangular sum of an array.

        :param nums: A list of integers.
        :return: The triangular sum of the array.
        """
        numElements = len(nums)

        while numElements > 1:
            for i in range(numElements - 1):
                nums[i] = (nums[i] + nums[i + 1]) % 10

            # Decrease the effective size of the array for the next iteration.
            numElements -= 1

        # The last remaining element is the triangular sum.
        return nums[0]