# Leetcode 2909: Minimum Sum of Mountain Triplets II
# https://leetcode.com/problems/minimum-sum-of-mountain-triplets-ii/
# Solved on 30th of November, 2025
class Solution:
    def minimumSum(self, nums: list[int]) -> int:
        """
        Finds the minimum sum of a mountain triplet (i, j, k) such that i < j < k
        and nums[i] < nums[j] and nums[k] < nums[j].

        Args:
            nums (list[int]): The input list of integers.

        Returns:
            int: The minimum sum of a mountain triplet, or -1 if no such triplet exists.
        """
        n = len(nums)
        suffixMin = [0] * n
        suffixMin[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            suffixMin[i] = min(nums[i], suffixMin[i + 1])

        minSum = float('inf')
        prefixMin = nums[0]

        for i in range(1, n - 1):
            currentVal = nums[i]
            rightMin = suffixMin[i + 1]

            if prefixMin < currentVal and rightMin < currentVal:
                minSum = min(minSum, prefixMin + currentVal + rightMin)

            prefixMin = min(prefixMin, currentVal)

        if minSum == float('inf'):
            return -1

        return minSum