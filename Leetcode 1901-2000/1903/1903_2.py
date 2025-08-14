# Leetcode 1903: Largest Odd Number in String
# https://leetcode.com/problems/largest-odd-number-in-string/
# Solved on 14th of August, 2025
class Solution:
    def largestOddNumber(self, num: str) -> str:
        """
        Finds the largest odd number that is a prefix of the given string `num`.
        :param num: The input string representing a large number.
        :return: The largest odd number that is a prefix of `num`.
                 Returns an empty string if no odd digit is found.
        """
        for i in range(len(num) - 1, -1, -1):
            if num[i] in "13579":
                return num[:i + 1]
        return ""