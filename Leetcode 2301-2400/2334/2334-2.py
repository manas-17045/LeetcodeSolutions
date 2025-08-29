# Leetcode 2334: Subarray With Elements Greater Than Varying Threshold
# https://leetcode.com/problems/subarray-with-elements-greater-than-varying-threshold/
# Solved on 29th of August, 2025
class Solution:
    def validSubarraySize(self, nums: list[int], threshold: int) -> int:
        """
        Finds the length of a valid subarray. A subarray is valid if for some k,
        nums[k] * length_of_subarray > threshold, where nums[k] is the smallest element in the subarray.

        Args:
            nums (list[int]): The input list of integers.
            threshold (int): The threshold value.
        Returns:
            int: The length of a valid subarray, or -1 if no such subarray exists.
        """
        n = len(nums)
        # prev smaller element index(strictly smaller)
        prev_smaller = [-1] * n
        stack = []
        for i in range(n):
            # pop >= so remaining top is strictly smaller (or none)
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            prev_smaller[i] = stack[-1] if stack else -1
            stack.append(i)

        # Next smaller or equal element index
        next_smaller_eq = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            # pop > so remaining top is <= current (or none)
            while stack and nums[stack[-1]] > nums[i]:
                stack.pop()
            next_smaller_eq[i] = stack[-1] if stack else n
            stack.append(i)

        # Check for each element whether its maximal span satisfies condition
        for i in range(n):
            length = next_smaller_eq[i] - prev_smaller[i] - 1
            if nums[i] * length > threshold:
                return length

        return -1