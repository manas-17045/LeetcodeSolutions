# Leetcode 3512: Minimum Operations to Make Array Sum Divisible by K
# https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/
# Solved on 30th of November, 2025
class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        """
        Calculates the minimum number of operations to make the array sum divisible by k.
        An operation consists of changing an element in the array.

        Args:
            nums: A list of integers.
            k: An integer.
        Returns:
            An integer representing the minimum number of operations.
        """
        arraySum = sum(nums)
        return arraySum % k