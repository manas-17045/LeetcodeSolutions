# Leetcode 2262: Total Appeal of A String
# https://leetcode.com/problems/total-appeal-of-a-string/
# Solved on 6th of november, 2025
class Solution:
    def appealSum(self, s: str) -> int:
        """
        Calculates the total appeal of all substrings of a given string s.
        The appeal of a string is the number of distinct characters in it.

        Args:
            s (str): The input string.
        Returns:
            int: The total appeal of all substrings.
        """
        totalAppeal = 0
        lastSeen = [-1] * 26
        n = len(s)
        ordA = ord('a')

        for i in range(n):
            charIndex = ord(s[i]) - ordA

            j = lastSeen[charIndex]

            contribution = (i - j) * (n - i)

            totalAppeal += contribution

            lastSeen[charIndex] = i

        return totalAppeal