# Leetcode 3640: Trionic Array II
# https://leetcode.com/problems/trionic-array-ii/
# Solved on 4th of February, 2026
class Solution:
    def maxSumTrionic(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of a trionic subarray.

        :param nums: A list of integers.
        :return: The maximum sum found for a trionic sequence.
        """
        incOne = float('-inf')
        dec = float('-inf')
        incTwo = float('-inf')
        maxSum = float('-inf')

        for i in range(1, len(nums)):
            current = nums[i]
            previous = nums[i - 1]

            if current > previous:
                incTwo = current + max(dec, incTwo)
                incOne = current + max(previous, incOne)
                dec = float('-inf')
            elif current < previous:
                dec = current + max(incOne, dec)
                incOne = float('-inf')
                incTwo = float('-inf')
            else:
                incOne = float('-inf')
                dec = float('-inf')
                incTwo = float('-inf')

            maxSum = max(maxSum, incTwo)

        return int(maxSum)