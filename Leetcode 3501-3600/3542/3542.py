# Leetcode 3542: Minimum Operations to Convert All Elements to Zero
# https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/
# Solved on 10th of November, 2025
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        """
        Calculates the minimum number of operations to convert all elements in the given list to zero.

        Args:
            nums: A list of integers.
        Returns:
            The minimum number of operations required.
        """
        stack = []
        totalOperations = 0

        for currentNum in nums:
            if currentNum == 0:
                stack.clear()
                continue

            while stack and stack[-1] > currentNum:
                stack.pop()

            if not stack or stack[-1] < currentNum:
                stack.append(currentNum)
                totalOperations += 1

        return totalOperations