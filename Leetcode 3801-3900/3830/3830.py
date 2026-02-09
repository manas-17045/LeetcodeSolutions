# Leetcde 3830: Longest Alternating Subarray After Removing At Most One Element
# https://leetcode.com/problems/longest-alternating-subarray-after-removing-at-most-one-element/
# Solved on 9th of February, 2026
class Solution:
    def longestAlternating(self, nums: list[int]) -> int:
        """
        Finds the length of the longest alternating subarray after removing at most one element.
        An alternating subarray is one where the relationship between adjacent elements alternates
        between strictly increasing and strictly decreasing.

        :param nums: List of integers to analyze.
        :return: The length of the longest alternating subarray possible.
        """
        n = len(nums)
        if n == 1:
            return 1

        up = 1
        down = 1
        upSkip = 1
        downSkip = 1

        preUp = 1
        preDown = 1

        ans = 1

        for i in range(1, n):
            curUp = 1
            curDown = 1
            curUpSkip = 1
            curDownSkip = 1

            if nums[i] > nums[i - 1]:
                curUp = down + 1
                curUpSkip = downSkip + 1
            elif nums[i] < nums[i - 1]:
                curDown = up + 1
                curDownSkip = upSkip + 1

            if i >= 2:
                if nums[i] > nums[i - 2]:
                    curUpSkip = max(curUpSkip, preDown + 1)
                elif nums[i] < nums[i - 2]:
                    curDownSkip = max(curDownSkip, preUp + 1)

            ans = max(ans, curUp, curDown, curUpSkip, curDownSkip)

            preUp = up
            preDown = down

            up = curUp
            down = curDown
            upSkip = curUpSkip
            downSkip = curDownSkip

        return ans