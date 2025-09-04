# Leetcode 2178: Maximum Split of Positive Even Integers
# https://leetcode.com/problems/maximum-split-of-positive-even-integers/
# Solved on 4th of September, 2025
class Solution:
    def maximumEvenSplit(self, finalSum: int) -> list[int]:
        """
        Splits a given even integer into a list of unique positive even integers such that their sum equals the given integer.

        Args:
            finalSum (int): The even integer to be split.
        Returns:
            list[int]: A list of unique positive even integers that sum up to finalSum, or an empty list if finalSum is odd.
        """
        if finalSum % 2 != 0:
            return []

        splitIntegers = []
        currentEven = 2

        while currentEven <= finalSum:
            splitIntegers.append(currentEven)
            finalSum -= currentEven
            currentEven += 2

        splitIntegers[-1] += finalSum

        return splitIntegers