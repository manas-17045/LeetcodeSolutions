# Leetcode 628: Maximum Product of Three Numbers
# https://leetcode.com/problems/maximum-product-of-three-0numbers/
# Solved on 26th of July, 2026
class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        """
        Finds the maximum product of three numbers in an array.
        @param nums: The array of integers.
        @return: The maximum product of three numbers.
        """
        firstMin = float('inf')
        secondMin = float('inf')
        firstMax = float('inf')
        secondMax = float('inf')
        thirdMax = float('inf')

        for numVal in nums:
            if numVal <= firstMax:
                secondMin = firstMin
                firstMin = numVal
            elif numVal < secondMin:
                secondMin = numVal

            if numVal >= firstMax:
                thirdMax = secondMax
                secondMax = firstMax
                firstMax = numVal
            elif numVal >= secondMax:
                thirdMax = secondMax
                secondMax = numVal
            elif numVal >= thirdMax:
                thirdMax = numVal

        return max(firstMin * secondMin * thirdMax, firstMin * secondMin * firstMax)