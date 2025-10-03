# Leetcode 2967: Minimum Cost to Make Array Equalindromic
# https://leetcode.com/problems/minimum-cost-to-make-array-equalindromic/
# Solved on 3rd of October, 2025
class Solution:
    def minimumCost(self, nums: list[int]) -> int:
        """
        Calculates the minimum cost to make all numbers in `nums` equal to a palindrome.
        :param nums: A list of integers.
        :return: The minimum cost.
        """
        def isPalindrome(n):
            s = str(n)
            return s == s[::-1]

        def calcCost(target):
            return sum(abs(num - target) for num in nums)

        nums.sort()
        median = nums[len(nums) // 2]

        minCost = float('inf')

        left = median
        while left >= 0:
            if isPalindrome(left):
                minCost = min(minCost, calcCost(left))
                break
            left -= 1

        right = median
        while right <= 10 ** 9:
            if isPalindrome(right):
                minCost = min(minCost, calcCost(right))
                break
            right += 1

        searchRange = 1000
        for candidate in range(max(0, median - searchRange), median + searchRange + 1):
            if isPalindrome(candidate):
                minCost = min(minCost, calcCost(candidate))

        return minCost