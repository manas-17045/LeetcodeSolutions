# Leetcode 3355: Zero Array Transformation I
# https://leetcode.com/problems/zero-array-transformation-i/
# Solved on 20th of May, 2025

class Solution:
    def isZeroArray(self, nums: list[int], queries: list[list[int]]) -> bool:
        """
        Determines if an array can be transformed into a zero array given a set of queries.

        Args:
            nums: A list of integers representing the initial array.
            queries: A list of queries, where each query is a list [l, r] representing a range of indices.

        Returns:
            True if the array can be transformed into a zero array, False otherwise.
        """
        n = len(nums)
        diff = [0] * (n + 1)

        # Build the coverage difference array
        for l, r in queries:
            diff[l] += 1
            diff[r + 1] -= 1

        # Prefix-sum to get actual coverage counts
        cover = [0] * n
        running = 0
        for i in range(n):
            running += diff[i]
            cover[i] = running

        # Check feasibility
        for i, v in enumerate(nums):
            if cover[i] < v:
                return False

        return True