# Leetcode 3113: Find the Number of Subarrays Where Boundary Elements Are Maximum
# https://leetcode.com/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/
# Solved on 5th of August, 2025
class Solution:
    def numberOfSubarrays(self, nums: list[int]) -> int:
        """
        Finds the number of subarrays where boundary elements are maximum.

        Args:
            nums: A list of integers.
        Returns:
            The total number of such subarrays.
        """
        monoStack = []
        totalResult = 0
        for currentNum in nums:
            while monoStack and monoStack[-1][0] < currentNum:
                monoStack.pop()
            if monoStack and monoStack[-1][0] == currentNum:
                monoStack[-1][1] += 1
            else:
                monoStack.append([currentNum, 1])
            totalResult += monoStack[-1][1]

        return totalResult