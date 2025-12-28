# Leetcode 3676: Count Bowl Subarrays
# https://leetcode.com/problems/count-bowl-subarrays/
# Solved on 28th of December, 2025
class Solution:
    def bowlSubarrays(self, nums: list[int]) -> int:
        """
        Counts the number of "bowl" subarrays in the given list of integers.

        :param nums: A list of integers.
        :return: The number of bowl subarrays.
        """
        n = len(nums)
        prevGreater = [-1] * n
        nextGreater = [-1] * n
        stack = []

        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            if stack:
                prevGreater[i] = stack[-1]
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            if stack:
                nextGreater[i] = stack[-1]
            stack.append(i)

        count = 0
        for i in range(n):
            if prevGreater[i] != -1 and nextGreater[i] != -1:
                count += 1

        return count