# Leetcode 2233: Maximum Product After K Increments
# https://leetcode.com/problems/maximum-product-after-k-increments/
# Solved on 22nd of November, 2025
import heapq


class Solution:
    def maximumProduct(self, nums: list[int], k: int) -> int:
        """
        Calculates the maximum product of elements in a list after performing k increments.

        Args:
            nums: A list of integers.
            k: The number of increments allowed.
        Returns:
            The maximum product after k increments, modulo 10^9 + 7.
        """

        heapq.heapify(nums)

        for i in range(k):
            minValue = nums[0]
            heapq.heapreplace(nums, minValue + 1)

        modValue = 10 ** 9 + 7
        result = 1

        for number in nums:
            result = (result * number) % modValue

        return result