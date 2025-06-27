# Leetcode 915: Partition Array into Disjoint Intervals
# https://leetcode.com/problems/partition-array-into-disjoint-intervals/
# Solved on 27th of June, 2025
class Solution:
    def partitionDisjoint(self, nums: list[int]) -> int:
        """
        Partitions the array `nums` into two (left and right) non-empty subarrays
        such that every element in the left subarray is less than or equal to
        every element in the right subarray.

        Returns the length of the smallest such left subarray.
        """
        partitionLength = 1
        maxInLeft = nums[0]
        currentMax = nums[0]

        for i in range(1, len(nums)):
            currentMax = max(currentMax, nums[i])
            if nums[i] < maxInLeft:
                partitionLength = i + 1
                maxInLeft = currentMax

        return partitionLength