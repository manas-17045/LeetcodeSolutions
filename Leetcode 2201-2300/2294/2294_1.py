# Leetcode 2294: Partition Array Such That Maximum Difference is K
# https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/
# Solved on 19th of June, 2025

class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        """
        Partitions the array `nums` into one or more subsequences such that the difference between the maximum and minimum
        values in each subsequence is at most `k`.

        Args:
            nums: A list of integers.
            k: The maximum allowed difference between the maximum and minimum values in a partition.
        """
        nums.sort()

        numPartitions = 1
        minInCurrentPartition = nums[0]

        for i in range(1, len(nums)):
            currentNum = nums[i]
            if currentNum - minInCurrentPartition > k:
                numPartitions += 1
                minInCurrentPartition = currentNum

        return numPartitions