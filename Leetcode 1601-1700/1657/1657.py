# Leetcode 1657: Determine if Two Strings Are Close
# https://leetcode.com/problems/determine-if-two-strings-are-close/
# Solved on 4th of November, 2025
import collections


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        """
        Determines if two strings are "close" based on specific operations.

        Args:
            word1 (str): The first input string.
            word2 (str): The second input string.
        Returns:
            bool: True if the strings are close, False otherwise.
        """
        if len(word1) != len(word2):
            return False

        frequencyMap1 = collections.Counter(word1)
        frequencyMap2 = collections.Counter(word2)

        uniqueChars1 = set(frequencyMap1.keys())
        uniqueChars2 = set(frequencyMap2.keys())

        if uniqueChars1 != uniqueChars2:
            return False

        counts1 = sorted(frequencyMap1.values())
        counts2 = sorted(frequencyMap2.values())

        return counts1 == counts2