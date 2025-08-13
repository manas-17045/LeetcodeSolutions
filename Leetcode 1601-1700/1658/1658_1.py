# Leetcode 1658: Minimum Operations to Reduce X to Zero
# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
# Solved on 13th of August, 2025
class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        """
        Given an integer array nums and an integer x, return the minimum number of operations to remove
        the leftmost or rightmost element from nums such that the sum of the removed elements equals x.
        If it is impossible to do so, return -1.

        Args:
            nums (list[int]): The input array of integers.
            x (int): The target sum.
        Returns:
            int: The minimum number of operations, or -1 if impossible.
        """
        totalSum = sum(nums)
        targetSum = totalSum - x

        if targetSum < 0:
            return -1

        if targetSum == 0:
            return len(nums)

        maxLength = -1
        currentSum = 0
        left = 0

        for right in range(len(nums)):
            currentSum += nums[right]

            while currentSum > targetSum and left <= right:
                currentSum -= nums[left]
                left += 1

            if currentSum == targetSum:
                maxLength = max(maxLength, right - left + 1)

        if maxLength == -1:
            return -1
        else:
            return len(nums) - maxLength