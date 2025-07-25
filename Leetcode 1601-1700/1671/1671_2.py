# Leetcode 1671: Minimum Number of Removals to Make Mountain Array
# https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/
# Solved on 25th of July, 2025
from bisect import bisect_left


class Solution:
    def minimumMountainRemovals(self, nums: list[int]) -> int:
        """
        Calculates the minimum number of elements to remove to make the remaining array a mountain array.

        :param nums: A list of integers.
        :return: The minimum number of removals.
        """

        n = len(nums)
        # lis[i] = length of the longest strictly increasing subsequence ending at i
        lis = [0] * n
        tails = []  # tails[k] = smallest tail of an increasing subseq of length k+1
        for i, x in enumerate(nums):
            pos = bisect_left(tails, x)
            if pos == len(tails):
                tails.append(x)
            else:
                tails[pos] = x
            lis[i] = pos + 1

        # lds[i] = length of the longest strictly decreasing subsequence starting at i
        lds = [0] * n
        tails.clear()
        for i in range(n - 1, -1, -1):
            x = nums[i]
            pos = bisect_left(tails, x)
            if pos == len(tails):
                tails.append(x)
            else:
                tails[pos] = x
            lds[i] = pos + 1

        # Find the largest valid mountain (peak must have lis>1 and lds>1)
        best = 0
        for i in range(n):
            if lis[i] > 1 and lds[i] > 1:
                # subtract 1 because nums[i] counted twice
                best = max(best, lis[i] + lds[i] - 1)

        # We need to remove everything outside that best mountain subsequence
        return n - best