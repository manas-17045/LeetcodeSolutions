# Leetcode 3698: Split Array With Minimum Difference
# https://leetcode.com/problems/split-array-with-minimum-difference/
# Solved on 25th of November, 2025
class Solution:
    def splitArray(self, nums: list[int]) -> int:
        """
        Splits an array into two parts such that the absolute difference between their sums is minimized.

        Args:
            nums: A list of integers.
        Returns:
            The minimum absolute difference between the sums of the two parts.
        """
        n = len(nums)
        incLimit = 0
        while incLimit < n - 1 and nums[incLimit + 1] > nums[incLimit]:
            incLimit += 1

        decLimit = n - 1
        while decLimit > 0 and nums[decLimit - 1] > nums[decLimit]:
            decLimit -= 1

        startIdx = max(0, decLimit - 1)
        endIdx = min(n - 2, incLimit)

        if startIdx > endIdx:
            return -1

        totalSum = sum(nums)
        leftSum = sum(nums[:startIdx])
        minDiff = float('inf')

        for i in range(startIdx, endIdx + 1):
            leftSum += nums[i]
            rightSum = totalSum - leftSum
            diff = abs(leftSum - rightSum)
            if diff < minDiff:
                minDiff = diff

        return minDiff