# Leetcode 3634: Minimum Removals to Balance Array
# https://leetcode.com/problems/minimum-removals-to-balance-array/
# Solved on 28th of September, 2025
class Solution:
    def minRemoval(self, nums: list[int], k: int) -> int:
        """
        Calculates the minimum number of elements to remove from an array such that the remaining elements
        satisfy the condition: max(remaining_elements) <= min(remaining_elements) * k.

        :param nums: A list of integers.
        :param k: An integer multiplier.
        :return: The minimum number of elements to remove.
        """
        n = len(nums)
        if n <= 1:
            return 0

        nums.sort()
        r = 0
        maxLen = 1  # At least one element can remain
        for l in range(n):
            # Ensure r is at least l
            if r < l:
                r = l
            # Extend r as far as possible while maintaining nums[r] <= nums[l] * k
            while r + 1 < n and nums[r + 1] <= nums[l] * k:
                r += 1
            # Update max length of a valid window
            maxLen = max(maxLen, r - l + 1)

        return n - maxLen