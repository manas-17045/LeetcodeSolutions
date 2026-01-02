# Leetcode 3297: Count Substrings That Can Be Rearranged to Contain a String I
# https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-i/
# Solved on 2nd of January, 2026
class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        """
        Counts the number of substrings in word1 that can be rearranged to form word2.

        Args:
            word1 (str): The main string to search within.
            word2 (str): The target string whose anagrams are to be counted as substrings.
        Returns:
            int: The total count of valid substrings.
        """
        n = len(word1)
        targetCounts = [0] * 26
        for char in word2:
            targetCounts[ord(char) - 97] += 1

        windowCounts = [0] * 26
        requiredChars = 0
        for count in targetCounts:
            if count > 0:
                requiredChars += 1

        formedChars = 0
        left = 0
        validCount = 0

        for right in range(n):
            charIndex = ord(word1[right]) - 97
            windowCounts[charIndex] += 1
            if windowCounts[charIndex] == targetCounts[charIndex]:
                formedChars += 1

            while formedChars == requiredChars:
                validCount += (n - right)
                leftCharIndex = ord(word1[left]) - 97
                windowCounts[leftCharIndex] -= 1
                if windowCounts[leftCharIndex] < targetCounts[leftCharIndex]:
                    formedChars -= 1
                left += 1

        return validCount