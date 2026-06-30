# Leetcode 1358: Number of Substrings Containing All Three Characters
# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
# Solved on 30th of June, 2026
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        """
        Computes the number of substrings that contain at least one 'a', 'b', and 'c'.
        
        @param s The input string.
        @return The number of substrings containing at least one 'a', 'b', and 'c'.
        """
        lastA = -1
        lastB = -1
        lastC = -1

        substringCount = 0
        for currentIndex, currentChar in enumerate(s):
            if currentChar == 'a':
                lastA = currentIndex
            elif currentChar == 'b':
                lastB = currentIndex
            elif currentChar == 'c':
                lastC = currentIndex
            substringCount += min(lastA, lastB, lastC) + 1
        
        return substringCount