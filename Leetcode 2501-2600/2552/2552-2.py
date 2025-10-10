# Leetcode 2552: Count Increasing Quadruplets
# https://leetcode.com/problems/count-increasing-quadruplets/
# Solved on 10th of October, 2025
class Solution:
    def countQuadruplets(self, nums: list[int]) -> int:
        """
        Counts the number of quadruplets (i, j, k, l) such that i < j < k < l, nums[i] < nums[k], nums[j] > nums[l], and nums[j] > nums[k].

        Args:
            nums: A list of integers.
        Returns:
            The number of such quadruplets.
        """
        n = len(nums)
        if n < 4:
            return 0

        greater_after = [[0] * n for _ in range(n)]

        # Build greater_after
        for j in range(1, n - 2):
            count = 0
            for l in range(j + 1, n):
                if nums[l] > nums[j]:
                    count += 1

            for k in range(j + 1, n - 1):
                if nums[j] > nums[k]:
                    greater_after[j][k] = count
                else:
                    count -= 1

        # Now, compute the answer while building the less_before on the fly
        ans = 0
        for k in range(2, n - 1):
            count = 0
            for i in range(k):
                if nums[i] < nums[k]:
                    count += 1
            for j in range(k - 1, 0, -1):
                if nums[j] > nums[k]:
                    ans += greater_after[j][k] * count
                else:
                    count -= 1

        return ans