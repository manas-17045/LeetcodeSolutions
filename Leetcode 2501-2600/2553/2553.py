# Leetcode 2553: Separate the Digits in an Array
# https://leetcode.com/problems/separate-the-digits-in-an-array/
# Solved on 11th of May, 2026
class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        """
        Separates each integer in the input list into its individual digits.

        :param nums: A list of positive integers.
        :return: A list of digits representing all numbers in nums in their original order.
        """
        resultArray = []

        for currentNum in nums:
            stringDigit = str(currentNum)
            for singleChar in stringDigit:
                resultArray.append(int(singleChar))

        return resultArray