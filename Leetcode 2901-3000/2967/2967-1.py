# Leetcode 2967: Minimum Cost to Make Array Equalindromic
# https://leetcode.com/problems/minimum-cost-to-make-array-equalindromic/
# Solved on 2nd of October, 2025
class Solution:
    def minimumCost(self, nums: list[int]) -> int:
        """
        Calculates the minimum cost to make all elements in the array equal to a palindromic number.
        :param nums: A list of integers.
        :return: The minimum cost.
        """
        def isPalindrome(n):
            return str(n) == str(n)[::-1]

        def calculateCost(target):
            totalCost = 0
            for num in nums:
                totalCost += abs(num - target)
            return totalCost

        nums.sort()
        listLength = len(nums)
        median = nums[listLength // 2]

        lowerPalindrome = median
        while not isPalindrome(lowerPalindrome):
            lowerPalindrome -= 1

        upperPalindrome = median
        while not isPalindrome(upperPalindrome):
            upperPalindrome += 1

        costForLower = calculateCost(lowerPalindrome)
        costForUpper = calculateCost(upperPalindrome)

        return min(costForLower, costForUpper)