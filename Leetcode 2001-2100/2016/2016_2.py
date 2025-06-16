# Leetcode 2016: Maximum Difference Between Increasing Elements
# https://leetcode.com/problems/maximum-difference-between-increasing-elements
# Solved on 16th of June, 2025

class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        """
        Given a 0-indexed integer array nums of size n, return the maximum difference between nums[i] and nums[j]
        such that 0 <= i < j < n and nums[i] < nums[j].

        Return -1 if no such pair exists.

        Args:
            nums: A list of integers.
        Returns:
            The maximum difference between nums[i] and nums[j] with i < j and nums[i] < nums[j], or -1 if no such pair exists.
        """
        # Initialize the minimum value to the first element
        min_val = nums[0]
        # Initialize max_diff to -1 (the "no valid pair" result)
        max_diff = -1

        # Iterate from the second element onward
        for num in nums[1:]:
            if num > min_val:
                # We found a valid increasing pair; update max_diff if better
                diff = num -min_val
                if diff > max_diff:
                    max_diff = diff
            else:
                # Update min_val to the new lower value
                min_val = num

        return max_diff