# Leetcode 3895: Count Digit Appearances
# https://leetcode.com/problems/count-digit-appearances/
# Solved on 19th of April, 2026
class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        """
        Counts the total number of times a specific digit appears across all integers in a list.

        :param nums: A list of integers to search through.
        :param digit: The specific digit (0-9) to count.
        :return: The total count of occurrences of the digit.
        """
        totalCount = 0
        for currentNumber in nums:
            while currentNumber > 0:
                if currentNumber % 10 == digit:
                    totalCount += 1

                currentNumber //= 10

        return totalCount