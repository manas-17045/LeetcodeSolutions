# Leetcode 3107: Minimum Operations to Make Median of Array Equal to K
# https://leetcode.com/problems/minimum-operations-to-make-median-of-array-equal-to-k/
# Solved on 18th of October, 2025
class Solution:
    def minOperationsToMakeMedianK(self, nums: list[int], k: int) -> int:
        """
        Calculates the minimum number of operations to make the median of the array equal to k.
        An operation consists of increasing or decreasing an element by 1.

        The median of an array of length n is the element at index n // 2 after sorting.

        Args:
            nums (list[int]): The input list of integers.
            k (int): The target median value.

        Returns:
            int: The minimum number of operations required.
        """
        nums.sort()
        n = len(nums)
        mid = n // 2
        ops = 0

        # For indices >= mid, values must be >= k (so increase those < k)
        for i in range(mid, n):
            if nums[i] < k:
                ops += k - nums[i]

        # For indices <= mid, values must be <= k (so decrease those > k)
        # Note: mid is included here; if nums[mid] > k it will be handled.
        for i in range(0, mid + 1):
            if nums[i] > k:
                ops += nums[i] - k

        return ops