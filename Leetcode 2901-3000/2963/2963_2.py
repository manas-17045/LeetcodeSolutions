# Leetcode 2963: Count the Number of Good Partitions
# https://leetcode.com/problems/count-the-number-of-good-partitions/
# Solved on 8th of August, 2025
class Solution:
    def numberOfGoodPartitions(self, nums: list[int]) -> int:
        """
        Calculates the number of good ways to partition an array `nums`.
        A partition is considered "good" if for every subarray in the partition,
        all elements that appear in that subarray appear only in that subarray.
        :param nums: A list of integers.
        :return: The number of good partitions modulo 10^9 + 7.
        """
        MOD = 10**9 + 7
        n = len(nums)
        if n <= 1:
            return 1

        # Record last occurrence index for each value
        last = {}
        for i, v in enumerate(nums):
            last[v] = i

        res = 1
        max_last = -1

        # Iterate and whenever current index equals max_last and not the final index,
        # We have a valid cut point -> choices double (cut or not).
        for i, v in enumerate(nums):
            if last[v] > max_last:
                max_last = last[v]
            if i == max_last and i != n - 1:
                res = (res * 2) % MOD

        return res