# Leetcode 2963: Count the Number of Good Partitions
# https://leetcode.com/problems/count-the-number-of-good-partitions/
# Solved on 8th of August, 2025
class Solution:
    def numberOfGoodPartitions(self, nums: list[int]) -> int:
        """
        Counts the number of good partitions of the given array `nums`.

        Args:
            nums (list[int]): The input array of integers.
        Returns:
            int: The number of good partitions modulo 10^9 + 7.
        """
        lastPos = {val: i for i, val in enumerate(nums)}

        result = 1
        mod = 10**9 + 7
        maxLastPos = 0

        for i in range(len(nums) - 1):
            maxLastPos = max(maxLastPos, lastPos[nums[i]])

            if i == maxLastPos:
                result = (result * 2) % mod

        return result