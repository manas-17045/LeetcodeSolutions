# Leetcode 2016: Maximum Difference Between Increasing Elements
# https://leetcode.com/problems/maximum-difference-between-increasing-elements
# Solved on 16th of June, 2025

class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        """
        Given a 0-indexed integer array nums of size n, return the maximum difference between nums[i] and nums[j] such that 0 <= i < j < n and nums[i] < nums[j]. If no such pair exists, return -1.

        Example 1:
        Input: nums = [7,1,5,4]
        Output: 4
        Explanation: The maximum difference occurs when i = 1 and j = 2, which is nums[j] - nums[i] = 5 - 1 = 4.
        Note that i = 1 and j = 0 is not considered because i < j.

        """
        maxDifference = -1
        minElement = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > minElement:
                maxDifference = max(maxDifference, (nums[i] - minElement))
            minElement = min(minElement, nums[i])
        return maxDifference