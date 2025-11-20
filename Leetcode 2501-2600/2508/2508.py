# Leetcode 2154: Keep Multiplying Found Values by Two
# https://leetcode.com/problems/keep-multiplying-found-values-by-two/
# Solved on 20th of November, 2025
class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        """
        Keeps multiplying the 'original' value by two as long as the multiplied value is found in 'nums'.

        :param nums: A list of integers to search within.
        :param original: The initial integer value.
        :return: The final integer value after all multiplications.
        """
        foundValues = set(nums)
        while original in foundValues:
            original *= 2
        return original