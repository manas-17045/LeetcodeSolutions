# Leetcode 2104: Sum of Subarray Ranges
# https://leetcode.com/problems/sum-of-subarray-ranges/
# Solved on 16th of November, 2025
class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:
        """
        Calculates the sum of ranges of all subarrays.

        Args:
            nums (list[int]): The input list of integers.
        Returns:
            int: The sum of (maximum - minimum) for all possible subarrays.
        """
        listLength = len(nums)
        totalSum = 0

        for i in range(listLength):
            currentMin = nums[i]
            currentMax = nums[i]
            for j in range(i, listLength):
                currentMin = min(currentMin, nums[j])
                currentMax = max(currentMax, nums[j])
                totalSum += (currentMax - currentMin)

        return totalSum