# Leetcode 1903: Largest Odd Number in String
# https://leetcode.com/problems/largest-odd-number-in-string/
# Solved on 14th of August, 2025
class Solution:
    def largestOddNumber(self, num: str) -> str:
        """
        Finds the largest odd number that is a substring of the given number string.

        Args:
            num (str): The input string representing a large number.

        Returns:
            str: The largest odd number as a substring, or an empty string if no odd number exists.
        """
        n = len(num)

        for i in range(n - 1, -1, -1):
            digit = int(num[i])
            if digit % 2 != 0:
                return num[:i + 1]

        return ""