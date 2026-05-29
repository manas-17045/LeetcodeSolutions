# Leetcode 3300: Minimum Element After Replacement With Digit Sum
# https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/
# Solved on 29th of May, 2026
class Solution:
    def minElement(self, nums: list[int]) -> int:
        """
        Calculates the minimum digit sum among all numbers in the given list.

        :param nums: A list of integers to process.
        :return: The smallest digit sum found.
        """
        minVal = float('inf')
        for num in nums:
            digitSum = 0
            while num > 0:
                digitSum += num % 10
                num //= 10

            if digitSum < minVal:
                minVal = digitSum

        return minVal