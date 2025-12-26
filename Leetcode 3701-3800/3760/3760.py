# Leetcode 3760: Maximum Substrings With Distinct Start
# https://leetcode.com/problems/maximum-substrings-with-distinct-start/
# Solved on 26th of December, 2025
class Solution:
    def maxDistinct(self, s: str) -> int:
        """
        This function calculates the number of distinct characters in a given string.

        :param s: The input string.
        :return: The count of distinct characters in the string.
        """
        distinctCharacters = set(s)
        return len(distinctCharacters)