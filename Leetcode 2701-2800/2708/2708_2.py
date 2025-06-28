# Leetcode 2708: Maximum Strength of a Group
# https://leetcode.com/problems/maximum-strength-of-a-group/
# Solved on 28th of June, 2025
class Solution:
    def maxStrength(self, nums: list[int]) -> int:
        """
        Calculates the maximum strength of a group, where strength is defined as the product of its elements.
        A group must be a non-empty subsequence of the given array `nums`.
        """
        n = len(nums)
        max_prod = float('-inf')

        # Enumerate all non-empty subsets via bitmasks 1...(1 << n) - 1
        for mask in range(1, (1 << n)):
            prod = 1
            # Multiply in every element whose bit is set
            for i in range(n):
                if mask & (1 << i):
                    prod *= nums[i]
            # Keep track of the best
            if prod > max_prod:
                max_prod = prod

        return max_prod