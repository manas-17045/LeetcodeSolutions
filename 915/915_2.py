# Leetcode 915: Partition Array into Disjoint Intervals
# https://leetcode.com/problems/partition-array-into-disjoint-intervals/
# Solved on 27th of June, 2025
class Solution:
    def partitionDisjoint(self, nums: list[int]) -> int:
        """
        Partitions an array `nums` into two (non-empty) disjoint subarrays, `left` and `right`,
        such that every element in `left` is less than or equal to every element in `right`.
        Returns the length of the `left` subarray.

        The algorithm iterates through the array, maintaining `maxInLeft` (the maximum element
        encountered so far in the potential left partition) and `currentMax` (the maximum element
        encountered in the entire array up to the current index).
        If an element `nums[i]` is found to be less than `maxInLeft`, it means that `nums[i]`
        must belong to the left partition, and thus the partition boundary must extend to at least `i + 1`.
        When this happens, `maxInLeft` is updated to `currentMax` because all elements up to `i`
        (including `nums[i]`) are now considered part of the left partition, and `currentMax`
        holds the true maximum of this extended left partition.
        """
        left_max = max_seen = nums[0]
        # partition_idx is the last index in the left partition
        partition_idx = 0

        for i in range(1, len(nums)):
            max_seen = max(max_seen, nums[i])
            if nums[i] < left_max:
                left_max = max_seen
                partition_idx = i

        # Length of left partition is index + 1
        return partition_idx + 1