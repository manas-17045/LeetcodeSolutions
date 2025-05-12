# Leetcode 1752: Check if Array Is Sorted and Rotated
# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

class Solution:
    def check(self, nums: list[int]) -> bool:
        m = len(nums)
        countA = 0
        for j in range(m):
            if nums[j] > nums[(j + 1) % m]:
                countA += 1
        return countA <= 1