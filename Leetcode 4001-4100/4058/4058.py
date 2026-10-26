# Leetcode 4058: Maximum Pulse Value After One Subarray Rotation
# https://leetcode.com/problems/maximum-pulse-value-after-one-subarray-rotation/
# Solved on 26th of October, 2026
class Solution:
    def maxValue(self, nums: list[int]) -> int:
        """
        Calculates the maximum pulse value of an array after at most one subarray left-rotation.

        Parameters:
            nums (List[int]): The list of integers.

        Returns:
            int: The maximum possible pulse value achievable.
        """
        currentPrefix = 0
        maxEvenPrefix = 0
        maxOddPrefix = None
        maxDiff = 0

        for itemIndex, numValue in enumerate(nums):
            if itemIndex % 2 == 0:
                currentPrefix += numValue
                if maxOddPrefix is not None:
                    maxDiff = max(maxDiff, maxOddPrefix - currentPrefix)
                    maxOddPrefix = max(maxOddPrefix, currentPrefix)
                else:
                    maxOddPrefix = currentPrefix
            else:
                currentPrefix -= numValue
                maxDiff = max(maxDiff, maxEvenPrefix - currentPrefix)
                maxEvenPrefix = max(maxEvenPrefix, currentPrefix)
                
        return currentPrefix + 2 * maxDiff