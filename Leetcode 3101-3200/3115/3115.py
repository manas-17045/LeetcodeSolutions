# Leetcode 3115: Maximum Prime Difference
# https://leetcode.com/problems/maximum-prime-difference/
# Solved on 6th of December, 2025
class Solution:
    def maximumPrimeDifference(self, nums: list[int]) -> int:
        """
        Calculates the maximum difference between the indices of two prime numbers in a given list.

        :param nums: A list of integers.
        :return: The maximum difference between the indices of two prime numbers.
        """
        primeSet = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
        firstIndex = -1
        lastIndex = -1

        for index, number in enumerate(nums):
            if number in primeSet:
                if firstIndex == -1:
                    firstIndex = index

                lastIndex = index

        return lastIndex - firstIndex