# Leetcode 1879: Minimum XOR Sum of Two Arrays
# https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/
# Solved on 10th of June, 2025

class Solution:
    def minimumXORSum(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Calculates the minimum XOR sum of two arrays.

        Given two integer arrays nums1 and nums2 of size n, we are allowed to
        rearrange the elements of nums2. We want to find the minimum possible
        XOR sum of the two arrays after rearranging the elements of nums2.
        The XOR sum of arrays nums1 and nums2 is defined as the bitwise XOR
        of all elements nums1[i] XOR nums2[i] for all i from 0 to n-1.

        Args:
            nums1: The first integer array.
            nums2: The second integer array.

        Returns:
            The minimum possible XOR sum of the two arrays.
        """
        n = len(nums1)
        dp = [float('inf')] * (1 << n)
        dp[0] = 0

        for mask in range(1, 1 << n):
            numPaired = bin(mask).count('1')
            i = numPaired - 1
            for j in range(n):
                if (mask >> j) & 1:
                    prevMask = mask ^ (1 << j)
                    currentSum = dp[prevMask] + (nums1[i] ^ nums2[j])
                    dp[mask] = min(dp[mask], currentSum)

        return int(dp[(1 << n) - 1])