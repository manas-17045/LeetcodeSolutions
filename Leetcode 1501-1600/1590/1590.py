# Leetcode 1590: Make Sum Divisible by P
# https://leetcode.com/problems/make-sum-divisible-by-p/
# Solved on 30th of November, 2025
class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        """
        Given an array of positive integers `nums`, and an integer `p`,
        return the length of the shortest subarray (can be empty) of `nums`
        such that removing this subarray makes the sum of the remaining elements
        divisible by `p`. If no such subarray exists, return -1.

        Args:
            nums (list[int]): The input array of positive integers.
            p (int): The integer by which the sum of remaining elements should be divisible.
        Returns:
            int: The length of the shortest subarray, or -1 if no such subarray exists.
        """
        totalSum = sum(nums)
        remainder = totalSum % p
        if remainder == 0:
            return 0

        modIndex = {0: -1}
        currentSum = 0
        minLength = len(nums)

        for i, num in enumerate(nums):
            currentSum = (currentSum + num) % p
            targetMod = (currentSum - remainder + p) % p

            if targetMod in modIndex:
                minLength = min(minLength, i - modIndex[targetMod])

            modIndex[currentSum] = i

        return minLength if minLength < len(nums) else -1