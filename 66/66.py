# Leetcode 66: Plus One
# https://leetcode.com/problems/plus-one/
# Solved on 1st of January, 2026
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        """
        Given a large integer represented as an integer array `digits`, where each `digits[i]` is the i-th digit of the integer.
        The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's, except for the number 0 itself.
        Increment the large integer by one and return the resulting array of digits.
        :param digits: A list of integers representing the large integer.
        :return: A list of integers representing the incremented large integer.
        """
        listLength = len(digits)
        for currentIndex in range(listLength - 1, -1, -1):
            if digits[currentIndex] < 9:
                digits[currentIndex] += 1

                return digits

            digits[currentIndex] = 0

        return [1] + digits