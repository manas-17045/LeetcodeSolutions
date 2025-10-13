# Leetcode 2273: Find Resultant Array After Removing Anagrams
# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/
# Solved on 13th of October, 2025
class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        """
        Removes consecutive anagrams from a list of words.

        Args:
            words: A list of strings.

        Returns:
            A list of strings with consecutive anagrams removed.
        """
        result = []
        lastKeptWordSorted = []

        for word in words:
            currentWordSorted = sorted(word)
            if currentWordSorted != lastKeptWordSorted:
                result.append(word)
                lastKeptWordSorted = currentWordSorted

        return result