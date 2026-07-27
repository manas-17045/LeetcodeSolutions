# Leetcode 1464: Maximum Product of Two Elements in an Array
# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
# Solved on 27th of July, 2026
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        """
        Finds the maximum product of two elements in an array, after subtracting 1 from each.

        @param nums: The input array of integers.
        @return: The maximum product of two elements in the array, after subtracting 1 from each.
        """
        firstMax = 0
        secondMax = 0

        for currentNum in nums:
            if currentNum > firstMax:
                secondMax = firstMax
                firstMax = currentNum
            elif currentNum > secondMax:
                secondMax = currentNum
        
        return (firstMax - 1) * (secondMax - 1)