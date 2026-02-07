# Leetcode 3825: Longest Strictly Increasing Subsequence With Non-Zero Bitwise AND
# https://leetcode.com/problems/longest-strictly-increasing-subsequence-with-non-zero-bitwise-and/
# Solved on 7th of February, 2026
import bisect


class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        """
        Finds the length of the longest strictly increasing subsequence where the bitwise AND of all elements is non-zero.

        :param nums: List of integers to process.
        :return: The length of the longest valid subsequence.
        """
        tails = [[] for _ in range(30)]

        for num in nums:
            for i in range(30):
                if (num >> i) & 1:
                    sub = tails[i]
                    idx = bisect.bisect_left(sub, num)

                    if idx < len(sub):
                        sub[idx] = num
                    else:
                        sub.append(num)

        return max(len(t) for t in tails)