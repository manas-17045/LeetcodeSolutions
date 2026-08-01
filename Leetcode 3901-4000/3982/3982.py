# Leetcode 3982: Sum of Integers with Maximum Digit Range
# https://leetcode.com/problems/sum-of-integers-with-maximum-digit-range/
# Solved on 1st of August, 2026
class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        """
        Calculates the sum of all integers in the input array that have the maximum
        digit range among all integers.
        
        The digit range of an integer is defined as the difference between its largest
        and smallest digits.
        
        Args:
            nums: A list of integers.
            
        Returns:
            The sum of all integers in the array that have the maximum digit range.
        """
        maxRange = -1
        totalSum = 0

        for numVal in nums:
            digitStr = str(numVal)
            currentRange = int(max(digitStr)) - int(min(digitStr))
            if currentRange > maxRange:
                maxRange = currentRange
                totalSum = numVal
            elif currentRange == maxRange:
                totalSum += numVal

        return totalSum