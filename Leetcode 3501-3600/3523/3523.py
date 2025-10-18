# Leetcode 3523: Make Array Non-decreasing
# https://leetcode.com/problems/make-array-non-decreasing/
# Solved on 18th of October, 2025
import sys
sys.setrecursionlimit(2000)


class Solution:
    def maximumPossibleSize(self, nums: list[int]) -> int:

        stack = []
        for num in nums:
            currentMax = num
            while stack and currentMax < stack[-1]:
                prevMax = stack.pop()
                currentMax = max(currentMax, prevMax)

            stack.append(currentMax)

        return len(stack)
