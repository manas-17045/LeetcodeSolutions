# Leetcode 2200: Find All K-Distant Indices in an Array
# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/
# Solved on 24th of June, 2025
class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        """
        Given a 0-indexed integer array nums, two integers key and k, return a list of all
        indices i such that there exists at least one index j such that |i - j| <= k and nums[j] == key.

        The returned list should be sorted in ascending order.

        This solution uses a difference array to efficiently mark all indices that are
        within k distance of any 'key' element.

        Args:
            nums: The input list of integers.
            key: The integer value to search for.
            k: The maximum allowed distance from an index j where nums[j] == key.

        Returns:
            A sorted list of indices i that satisfy the condition.
        """
        n = len(nums)
        # diff[i] will track how many "ranges" start/end at i
        diff = [0] * (n + 1)

        # For each index j where nums[j] == key, we want to mark [(j - k), (j + k)]
        for j, v in enumerate(nums):
            if v == key:
                left = max(0, (j - k))
                right = min((n - 1), (j + k))
                diff[left] += 1
                diff[right + 1] -= 1

        # Build the coverage array: cov[i] > 0 iff i is within k of some key
        cov = [0] * n
        cur = 0
        for i in range(n):
            cur += diff[i]
            cov[i] = cur

        # Collect all i where cov[i] > 0
        return [i for i in range(n) if cov[i] > 0]