# Leetcode 2354: Number of Excellent Pairs
# https://leetcode.com/problems/number-of-excellent-pairs/
# Solved on 28th of November, 2025
class Solution:
    def countExcellentPairs(self, nums: list[int], k: int) -> int:
        """
        Counts the number of excellent pairs (a, b) such that a and b are from `nums`,
        and the sum of their bit counts (a | b).bit_count() + (a & b).bit_count() >= k.

        :param nums: A list of integers.
        :param k: An integer threshold.
        :return: The total number of excellent pairs.
        """
        uniqueNums = set(nums)
        bitCounts = [0] * 32
        for num in uniqueNums:
            bitCounts[num.bit_count()] += 1

        totalPairs = 0
        for i in range(32):
            if bitCounts[i] > 0:
                for j in range(max(0, k - i), 32):
                    totalPairs += bitCounts[i] * bitCounts[j]

        return totalPairs