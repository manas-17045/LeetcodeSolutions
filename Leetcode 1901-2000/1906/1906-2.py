# Leetcode 1906: Minimum Absolute Difference Queries
# https://leetcode.com/problems/minimum-absolute-difference-queries/
# Solved on 25th of September, 2025
class Solution:
    def minDifference(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        """
        Calculates the minimum absolute difference between any two distinct elements
        within specified ranges for multiple queries.

        Args:
            nums: A list of integers.
            queries: A list of [left, right] pairs representing query ranges.
        Returns:
            A list of integers, where each element is the minimum difference for the
            corresponding query, or -1 if there's only one unique number in the range.
        """
        n = len(nums)

        prefix = [[0] * 101 for _ in range(n + 1)]

        for i, val in enumerate(nums):
            # Copy previous counts
            row = prefix[i + 1]
            prev = prefix[i]
            row[:] = prev[:]
            row[val] += 1

        res = []
        for l, r in queries:
            # Get counts of each value in nums[l...r]
            cnt = [prefix[r + 1][v] - prefix[l][v] for v in range(1, 101)]
            prev_val = -1
            min_diff = 10**9
            # Iterate values 1...100
            for v_idx, c in enumerate(cnt, start=1):
                if c > 0:
                    if prev_val != -1:
                        diff = v_idx - prev_val
                        if diff < min_diff:
                            min_diff = diff
                            # Early exit if zero (can't be less)
                            if diff == 0:
                                break
                    prev_val = v_idx

            # If only one unique value, return -1.
            res.append(-1 if min_diff == 10**9 else min_diff)

        return res