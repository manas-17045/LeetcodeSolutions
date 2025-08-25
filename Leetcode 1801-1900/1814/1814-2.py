# Leetcode 1814: Count Nice Pairs in an Array
# https://leetcode.com/problems/count-nice-pairs-in-an-array/
# Solved on 25th of August, 2025
from collections import defaultdict


class Solution:
    def countNicePairs(self, nums: list[int]) -> int:
        """
        Counts the number of "nice pairs" in a given list of integers.
        A pair (i, j) is considered nice if nums[i] + rev(nums[j]) == nums[j] + rev(nums[i]),
        which simplifies to nums[i] - rev(nums[i]) == nums[j] - rev(nums[j]).
        :param nums: A list of integers.
        :return: The number of nice pairs modulo 10^9 + 7.
        """
        MOD = 10 ** 9 + 7

        def rev(x: int) -> int:
            r = 0
            while x:
                r = r * 10 + (x % 10)
                x //= 10
            return r

        counts = defaultdict(int)
        for x in nums:
            diff = x - rev(x)
            counts[diff] += 1

        ans = 0
        for c in counts.values():
            ans = (ans + c * (c - 1) // 2) % MOD

        return ans