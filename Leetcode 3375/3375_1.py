# Leetcode 3375: Minimum Operations to Make Array Values Equal to K
# https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/
# Submitted on April 9, 2025

class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        """
        Calculates the minimum number of operations required to make all unique
        numbers in the input list less than or equal to a given threshold value.

        :param nums: The list of integers to process.
        :param k: The threshold value to compare the unique numbers against.
        :return: The minimum number of operations needed to reduce all unique
            numbers greater than the threshold value, or -1 if any number in the
            list is initially less than the threshold.
        """
        if any(num < k for num in nums):
            return -1

        unique_nums = set(nums)

        operations = 0
        for unique_num in unique_nums:
            if unique_num > k:
                operations += 1

        return operations