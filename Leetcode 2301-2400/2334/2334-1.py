# Leetcode 2334: Subarray With Elements Greater Than Varying Threshold
# https://leetcode.com/problems/subarray-with-elements-greater-than-varying-threshold/
# Solved on 29th of August, 2025
class Solution:
    def validSubarraySize(self, nums: list[int], threshold: int) -> int:
        """
        Finds the length of a valid subarray such that for some element `x` in the subarray,
        `x * k > threshold`, where `k` is the length of the subarray, and `x` is the minimum
        element in that subarray.

        Args:
            nums (list[int]): The input list of integers.
            threshold (int): The threshold value.
        Returns:
            int: The length of a valid subarray, or -1 if no such subarray exists.
        """
        n = len(nums)

        prevLess = [-1] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                prevLess[i] = stack[-1]
            stack.append(i)

        nextLess = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                nextLess[i] = stack[-1]
            stack.append(i)

        for i in range(n):
            subLength = nextLess[i] - prevLess[i] - 1
            if nums[i] * subLength > threshold:
                return subLength

        return -1