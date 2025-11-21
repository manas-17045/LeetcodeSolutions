# Leetcode 3738: Longest Non-Decreasing Subarray After Replacing at Most One Element
# https://leetcode.com/problems/longest-non-decreasing-subarray-after-replacing-at-most-one-element/
# Solved on 21st of November, 2025
class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        """
        Calculates the length of the longest non-decreasing subarray after replacing at most one element.

        Args:
            nums (list[int]): The input list of integers.
        Returns:
            int: The length of the longest non-decreasing subarray.
        """
        n = len(nums)
        if n == 1:
            return 1

        leftLengths = [1] * n
        rightLengths = [1] * n

        for i in range(1, n):
            if nums[i] >= nums[i - 1]:
                leftLengths[i] = leftLengths[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                rightLengths[i] = rightLengths[i + 1] + 1

        maxLength = max(leftLengths)

        for i in range(n):
            leftPart = leftLengths[i - 1] if i > 0 else 0
            rightPart = rightLengths[i + 1] if i < n - 1 else 0

            currentLength = max(leftPart + 1, rightPart + 1)

            if i > 0 and i < n - 1 and nums[i + 1] >= nums[i - 1]:
                currentLength = max(currentLength, leftPart + 1 + rightPart)

            maxLength = max(maxLength, currentLength)

        return maxLength