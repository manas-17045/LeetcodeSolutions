# Leetcode 2009: Minimum Number of Operations to Make Array Continuous
# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/
# Solved on 17th of May, 2025

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        """
        Given an integer array nums, return the minimum number of operations it takes to make nums continuous.

        In one operation, you can replace any number in nums with any integer.

        nums is continuous if, after sorting, it contains consecutive integers.
        For example, nums = [4, 2, 5, 3] is continuous, but nums = [1, 2, 3, 5, 6] is not continuous.
        """
        n = len(nums)
        # Work with unique sorted values
        uniq = sorted(set(nums))

        max_in_window = 0
        i = 0
        # Sliding window over uniq such that uniq[j] - uniq[i] <= n - 1
        for j, v in enumerate(uniq):
            # Shrink from left if span too large
            while v - uniq[i] > n - 1:
                i += 1
            # Number of unique values in [i..j]
            window_size = j - i + 1
            if window_size > max_in_window:
                max_in_window = window_size

        # We want n distinct consecutive values.
        # We already have max_in_window good ones, so need to change the rest.
        return n - max_in_window