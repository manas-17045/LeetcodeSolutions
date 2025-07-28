# Leetcode 1392: Longest Happy Prefix
# https://leetcode.com/problems/longest-happy-prefix/
# Solved on 28th of July, 2025
class Solution:
    def longestPrefix(self, s: str) -> str:
        """
        Finds the longest happy prefix of a given string.
        A string is a "happy prefix" if it is a non-empty prefix of the original string
        and also a suffix of the original string.

        Args:
            s (str): The input string.
        Returns:
            str: The longest happy prefix.
        """

        strLen = len(s)
        lpsArray = [0] * strLen
        prevLpsLen = 0
        currentIndex = 1

        while currentIndex < strLen:
            if s[currentIndex] == s[prevLpsLen]:
                prevLpsLen += 1
                lpsArray[currentIndex] = prevLpsLen
                currentIndex += 1
            else:
                if prevLpsLen != 0:
                    prevLpsLen = lpsArray[prevLpsLen - 1]
                else:
                    lpsArray[currentIndex] = 0
                    currentIndex += 1

        resultLen = lpsArray[-1] if strLen > 0 else 0
        return s[:resultLen]