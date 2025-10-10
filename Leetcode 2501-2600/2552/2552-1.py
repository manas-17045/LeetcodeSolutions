# Leetcode 2552: Count Increasing Quadruplets
# https://leetcode.com/problems/count-increasing-quadruplets/
# Solved on 10th of October, 2025
class Solution:
    def countQuadruplets(self, nums: list[int]) -> int:
        """
        Counts the number of increasing quadruplets (i, j, k, l) such that i < j < k < l
        and nums[i] < nums[k] < nums[j] < nums[l].

        Args:
            nums: A list of integers.
        Returns:
            The total number of increasing quadruplets.
        """
        n = len(nums)
        if n < 4:
            return 0

        greater = [[0] * (n + 1) for _ in range(n + 1)]
        for k in range(n - 1, -1, -1):
            greater[k][:] = greater[k + 1][:]
            val = nums[k]
            for v in range(1, val):
                greater[k][v] += 1

        totalQuadruplets = 0
        less = [0] * (n + 1)

        for j in range(1, n - 1):
            prevVal = nums[j - 1]
            for v in range(prevVal + 1, n + 1):
                less[v] += 1

            for k in range(j + 1, n - 1):
                if nums[j] > nums[k]:
                    countLess = less[nums[k]]
                    countGreater = greater[k][nums[j]]
                    totalQuadruplets += countLess * countGreater

        return totalQuadruplets