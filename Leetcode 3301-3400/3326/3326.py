# Leetcode 3326: Minimum Division Operations to make Array Non Decreasing
# https://leetcode.com/problems/minimum-division-operations-to-make-array-non-decreasing/
# Solved on 29th of November, 2025
maxVal = 1000002
spf = list(range(maxVal))
for i in range(2, int(maxVal ** 0.5) + 1):
    if spf[i] == i:
        for j in range(i * i, maxVal, i):
            if spf[j] == j:
                spf[j] = i


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        """
        Calculates the minimum number of operations to make the array non-decreasing.

        Args:
            nums: A list of integers.
        Returns:
            The minimum number of operations, or -1 if it's impossible.
        """
        n = len(nums)
        count = 0
        for i in range(n - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                primeFactor = spf[nums[i]]
                if nums[i] == primeFactor:
                    return -1
                nums[i] = primeFactor
                count += 1
                if nums[i] > nums[i + 1]:
                    return -1
        return count
