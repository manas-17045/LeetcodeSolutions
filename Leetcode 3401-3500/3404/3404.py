# Leetcode 3404: Count Special Subsequences
# https://leetcode.com/problems/count-special-subsequences/
# Solved on 4th of December, 2025
from collections import defaultdict
from math import gcd


class Solution:
    def numberOfSubsequences(self, nums: list[int]) -> int:
        """
        Counts the number of special subsequences in the given list of integers.

        Args:
            nums: A list of integers.
        Returns:
            The total count of special subsequences.
        """
        n = len(nums)
        ans = 0
        ratioCnt = defaultdict(int)

        for r in range(4, n - 2):
            q = r - 2
            for p in range(q - 1):
                valP = nums[p]
                valQ = nums[q]
                common = gcd(valP, valQ)
                key = (valP // common, valQ // common)
                ratioCnt[key] += 1

            valR = nums[r]
            for s in range(r + 2, n):
                valS = nums[s]
                common = gcd(valS, valR)
                key = (valS // common, valR // common)
                ans += ratioCnt[key]

        return ans