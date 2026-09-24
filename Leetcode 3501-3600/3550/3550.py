# Leetcode 3550: Smallest Index With Digit Sum Equal to Index
# https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/
# Solved on 24th of September, 2026
class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        """
        Calculate the sum of the digits of a non-negative integer.

        Parameters:
            numVal (int): The integer whose digits are to be summed.

        Returns:
            int: The sum of the digits.
        """
        for currentIndex, currentNum in enumerate(nums):
            if self.getDigitSum(currentNum) == currentIndex:
                return currentIndex

        return -1
    
    
    def getDigitSum(self, numVal: int) -> int:

        digitSum = 0
        tempVal = numVal
        while tempVal > 0:
            digitSum += tempVal % 10
            tempVal //= 10
        return digitSum