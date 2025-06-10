# Leetcode 1879: Minimum XOR Sum of Two Arrays
# https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/
# Solved on 10th of June, 2025

class Solution:
    def minimumXORSum(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Given two integer arrays nums1 and nums2 of size n, return the minimum XOR sum of the arrays.

        The XOR sum of a pair of arrays is defined as the sum of the XORs of corresponding elements.
        Specifically, if we have a permutation p of [0, 1, ..., n - 1] which maps elements of nums1 to elements of nums2,
        the XOR sum is nums1[0] XOR nums2[p[0]] + nums1[1] XOR nums2[p[1]] + ... + nums1[n - 1] XOR nums2[p[n - 1]].

        This problem can be solved using dynamic programming with bitmask.
        The state dp[mask] represents the minimum XOR sum for the first `mask.bit_count()` elements of nums1, where the mask indicates which elements of nums2 have been used.
        """
        n = len(nums1)
        full_mask = (1 << n) - 1

        # Precompute costs to avoid recomputing XOR every time
        cost = [[nums1[i] ^ nums2[j] for j in range(n)] for i in range(n)]

        dp = [float('inf')] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            # How many nums1 we've already paired
            i = mask.bit_count()
            if i == n:
                continue
            # Try pairing nums1[i] with any nums2[j] not yet used in mask
            for j in range(n):
                if not (mask & (1 << j)):
                    newMask = mask | (1 << j)
                    dp[newMask] = min(dp[newMask], dp[mask] + cost[i][j])

        return int(dp[full_mask])