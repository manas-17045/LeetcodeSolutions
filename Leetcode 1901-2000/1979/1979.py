# Leetcode 1979: Find Greatest Common Divisor of Array
# https://leetcode.com/problems/find-greatest-common-divisor-of-array/
# Solved on 18th of July, 2026
class Solution:
    def findGCD(self, nums: list[int]) -> int:
        """
        Finds the greatest common divisor of the smallest and largest numbers in the array.

        Args:
            nums: The input array of integers.

        Returns:
            The greatest common divisor of the smallest and largest numbers in the array.
        """
        minVal = min(nums)
        maxVal = max(nums)
        while minVal:
            maxVal, minVal = minVal, maxVal % minVal
        
        return maxVal