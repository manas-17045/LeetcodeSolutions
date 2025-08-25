# Leetcode 1814: Count Nice Pairs in an Array
# https://leetcode.com/problems/count-nice-pairs-in-an-array/
# Solved on 25th of August, 2025
from collections import defaultdict


class Solution:
    def countNicePairs(self, nums: list[int]) -> int:
        """
        Counts the number of "nice" pairs in the given array.
        A pair (i, j) is considered nice if nums[i] + rev(nums[j]) == nums[j] + rev(nums[i]),
        which simplifies to nums[i] - rev(nums[i]) == nums[j] - rev(nums[j]).
        :param nums: A list of integers.
        :return: The number of nice pairs modulo 10^9 + 7.
        """
        def rev(n: int) -> int:
            return int(str(n)[::-1])

        freqMap = defaultdict(int)
        nicePairsCount = 0
        mod = 10 ** 9 + 7

        for num in nums:
            diff = num - rev(num)
            nicePairsCount = (nicePairsCount + freqMap[diff]) % mod
            freqMap[diff] += 1

        return nicePairsCount