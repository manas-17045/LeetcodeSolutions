# Leetcode 2366: Minimum Replacements to Sort the Array
# https://leetcode.com/problems/minimum-replacements-to-sort-the-array/
# Solved on 5th of December, 2025
class Solution:
    def minimumReplacement(self, nums: list[int]) -> int:
        """
        Calculates the minimum number of replacements needed to sort the array in non-decreasing order.

        Args:
            nums (list[int]): The input array of integers.
        Returns:
            int: The minimum number of replacements.
        """
        totalOperations = 0
        currentBound = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            currentValue = nums[i]
            if currentValue > currentBound:
                numberOfParts = (currentValue + currentBound - 1) // currentBound
                totalOperations += numberOfParts - 1
                currentBound = currentValue // numberOfParts
            else:
                currentBound = currentValue

        return totalOperations