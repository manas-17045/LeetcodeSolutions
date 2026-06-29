# Leetcode 1967: Number of Strings That Appear as Substrings in Word
# https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/
# Solved on 29th of June, 2026
class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        """
        Checks the number of strings in the given array of patterns that appear as substrings in the given word.
        @param patterns: The array of patterns to check.
        @param word: The word to check for substrings.
        @return: The number of patterns that appear as substrings in the word.
        """
        matchCount = 0
        for currentPattern in patterns:
            if currentPattern in word:
                matchCount += 1
        
        return matchCount