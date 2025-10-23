# Leetcode 3298: Count Substrings That Can Be Rearranged to Contain a String II
# https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-ii/
# Solved on 23rd of October, 2025
class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        """
        Counts the number of substrings in word1 that can be rearranged to form word2.

        Args:
            word1 (str): The main string to search within.
            word2 (str): The target string whose anagrams are to be counted.

        Returns:
            int: The total number of valid substrings.
        """
        lenWord1 = len(word1)
        lenWord2 = len(word2)

        if lenWord1 < lenWord2:
            return 0

        countWord2 = [0] * 26
        requiredDistinctChars = 0

        for char in word2:
            charIndex = ord(char) - ord('a')
            if countWord2[charIndex] == 0:
                requiredDistinctChars += 1
            countWord2[charIndex] += 1

        totalValidSubstrings = 0
        left = 0
        currentWindowCount = [0] * 26
        satisfiedDistinctChars = 0

        for right in range(lenWord1):
            rightCharIndex = ord(word1[right]) - ord('a')
            currentWindowCount[rightCharIndex] += 1

            if countWord2[rightCharIndex] > 0 and currentWindowCount[rightCharIndex] == countWord2[rightCharIndex]:
                satisfiedDistinctChars += 1

            while satisfiedDistinctChars == requiredDistinctChars and left <= right:
                leftCharIndex = ord(word1[left]) - ord('a')

                if countWord2[leftCharIndex] > 0 and currentWindowCount[leftCharIndex] == countWord2[leftCharIndex]:
                    satisfiedDistinctChars -= 1

                currentWindowCount[leftCharIndex] -= 1
                left += 1

            totalValidSubstrings += left

        return totalValidSubstrings