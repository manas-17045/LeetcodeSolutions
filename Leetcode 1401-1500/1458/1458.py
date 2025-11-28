# Leetcode 1458: Max Dot Product of Two Subsequences
# https://leetcode.com/problems/max-dot-product-of-two-subsequences/
# Solved on 28th of November, 2025
class Solution:
    def maxDotProduct(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Calculates the maximum dot product of two non-empty subsequences from nums1 and nums2.

        Args:
            nums1: The first list of integers.
            nums2: The second list of integers.
        Returns:
            The maximum dot product.
        """
        n = len(nums1)
        m = len(nums2)
        dp = [float('-inf')] * m

        for i in range(n):
            currentDp = [float('-inf')] * m
            for j in range(m):
                product = nums1[i] * nums2[j]

                prevDiagonal = dp[j - 1] if j > 0 else float('-inf')
                prevTop = dp[j]
                prevLeft = currentDp[j - 1] if j > 0 else float('-inf')

                currentDp[j] = max(product, prevDiagonal + product, prevTop, prevLeft)
            dp = currentDp

        return int(dp[-1])