# Leetcode 3077: Maximum Strength of K Disjoint Subarrays
# https://leetcode.com/problems/maximum-strength-of-k-disjoint-subarrays/
# Solved on 28th of June, 2025
class Solution:
    def maxStrength(self, nums: list[int], k: int) -> int:
        """
        Calculates the maximum strength of k disjoint subarrays.

        The strength of a set of k disjoint subarrays is defined as the sum of
        (k - j + 1) * (-1)^(j+1) * (sum of elements in j-th subarray) for j from 1 to k.

        Args:
            nums: A list of integers representing the array.
            k: An integer representing the number of disjoint subarrays.

        Returns:
            An integer representing the maximum strength.
        """
        n = len(nums)

        fPrev = [0] * (n + 1)

        for j in range(1, (k + 1)):
            e = float('-inf')
            fCurr = [float('-inf')] * (n + 1)

            sign = -1 if j % 2 == 0 else 1
            coeff = (k - j + 1) * sign

            for i in range(j, (n + 1)):
                e = max(e, fPrev[i - 1]) + (coeff * nums[i - 1])

                fCurr[i] = max(fCurr[i - 1], e)

            fPrev = fCurr

        return int(fPrev[n])