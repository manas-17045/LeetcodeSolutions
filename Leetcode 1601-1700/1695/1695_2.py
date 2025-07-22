# Leetcode 1695: Maximum Erasure Value
# https://leetcode.com/problems/maximum-erasure-value/
# Solved on 22nd of July, 2025
class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        """
        Calculates the maximum sum of a unique subarray.

        Args:
            nums (list[int]): The input list of integers.
        Returns:
            int: The maximum sum of a subarray with unique elements.
        """
        seen = set()
        left = 0
        curr_sum = 0
        max_sum = 0

        for right, x in enumerate(nums):
            # if x is already in our window, shrink from the left
            while x in seen:
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1

            # Add the new unique element
            seen.add(x)
            curr_sum += x

            # Update the best score so far
            if curr_sum > max_sum:
                max_sum = curr_sum

        return max_sum