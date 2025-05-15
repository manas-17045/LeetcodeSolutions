# Leetcode 1726: Tuple with Same Product
# https://leetcode/problems/tuple-with-same-product/
# Solved on 14th of May, 2025

from collections import defaultdict


class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        """
        Given a list of distinct integers, return the number of tuples (a, b, c, d)
        such that a * b = c * d where a, b, c, and d are distinct elements of nums.

        Args:
            nums: A list of distinct integers.
        Returns:
            The number of tuples satisfying the condition.
        """
        # Count how many unordered pairs (i < j) yield each product
        prod_count = defaultdict(int)
        n = len(nums)
        for i in range(n):
            ai = nums[i]
            for j in range(i + 1, n):
                prod_count[ai * nums[j]] += 1

        # For each product with c pairs, we can pick two distinct pairs
        # in c × (c - 1) ways (order of pair-selection matters),
        # and within each pair, we can swap the two elements (2 ways each).
        # Total multiplicity per product = c×(c - 1)×2×2 = c×(c - 1)×4
        ans = 0
        for c in prod_count.values():
            if c > 1:
                ans += c * (c - 1) * 4

        return ans