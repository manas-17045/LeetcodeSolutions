# Leetcode 3659: Partition Array Into K-Distinct Groups
# https://leetcode.com/problems/partition-array-into-k-distinct-groups/
# Solved on 1st of November, 2025
from collections import Counter


class Solution:
    def partitionArray(self, nums: list[int], k: int) -> bool:
        """
        Determines if an array can be partitioned into k distinct groups.

        Args:
            nums (list[int]): The input list of integers.
            k (int): The number of distinct groups.
        Returns:
            bool: True if the array can be partitioned, False otherwise.
        """

        totalSize = len(nums)

        if totalSize % k != 0:
            return False

        numGroups = totalSize // k

        counts = Counter(nums)

        for freq in counts.values():
            if freq > numGroups:
                return False

        return True