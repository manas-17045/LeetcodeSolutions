# Leetcode 3289: The Two Sneaky Numbers of Digitville
# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/
# Solved on 31st of October, 2025
class Solution:
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        """
        Identifies and returns numbers that appear more than once in the input list.

        :param nums: A list of integers.
        :return: A list of integers that are "sneaky" (i.e., duplicates).
        """
        seenNumbers = set()
        sneakyNumbers = []

        for currentNum in nums:
            if currentNum in seenNumbers:
                sneakyNumbers.append(currentNum)
            else:
                seenNumbers.add(currentNum)

        return sneakyNumbers