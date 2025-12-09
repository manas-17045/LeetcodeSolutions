# Leetcode 3583: Count Special Triplets
# https://leetcode.com/problems/count-special-triplets/
# Solved on 9th of December, 2025
from collections import defaultdict


class Solution:
    def specialTriplets(self, nums: list[int]) -> int:
        """
        Counts the number of "special triplets" (a, b, c) in the given list of integers `nums`.
        A triplet (a, b, c) is considered special if a * 2 = b and b * 2 = c.

        Args:
            nums: A list of integers.
        Returns:
            The total count of special triplets modulo 10^9 + 7.
        """
        rightCounts = defaultdict(int)
        for num in nums:
            rightCounts[num] += 1

        leftCounts = defaultdict(int)
        totalCount = 0
        modulo = 10 ** 9 + 7

        for num in nums:
            rightCounts[num] -= 1
            target = num * 2

            totalCount = (totalCount + leftCounts[target] * rightCounts[target]) % modulo

            leftCounts[num] += 1

        return totalCount