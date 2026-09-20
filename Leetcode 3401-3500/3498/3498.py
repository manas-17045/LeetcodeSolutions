# Leetcode 3498: Reverse Degree of a String
# https://leetcode.com/problems/reverse-degree-of-a-string/
# Solved on 20th of September, 2026
class Solution:
    def reverseDegree(self, s: str) -> int:
        """
        Calculates the reverse degree of a string based on reverse alphabet ordering.

        Parameters:
            s (str): The input string containing lowercase English letters.

        Returns:
            int: The total sum of each character's reversed alphabet rank multiplied
            by its 1-based string position.
        """
        totalDegree = 0

        for stringIndex, charValue in enumerate(s, start=1):
            reversedRank = 26 - (ord(charValue) - ord('a'))
            totalDegree += reversedRank * stringIndex

        return totalDegree