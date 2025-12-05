# Leetcode 3432: Count Partitions with Even Sum Difference
# https://leetcode.com/problems/count-partitions-with-even-sum-difference/
# Solved on 5th of November, 2025
class Solution:
    def countPartitions(self, nums: list[int]) -> int:
        """
        Counts the number of ways to partition the array into two non-empty subarrays
        such that the absolute difference between their sums is even.
        :param nums: The input list of integers.
        :return: The number of valid partitions.
        """
        arraySum = sum(nums)
        if arraySum % 2 == 0:
            return len(nums) - 1

        return 0