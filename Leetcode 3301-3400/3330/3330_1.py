# Leetcode 3330: Find the Original Typed String I
# https://leetcode.com/problems/find-the-original-typed-string-i/
# Solved on 1st of July, 2025
class Solution:
    def possibleStringCount(self, word: str) -> int:
        """
        Calculates the number of possible original typed strings given a `word`
        where consecutive identical characters are counted as one.

        Args:
            word (str): The typed string.
        Returns:
            int: The count of possible original typed strings.
        """
        wordLength = len(word)
        totalCount = 1

        for currentIndex in range(1, wordLength):
            if word[currentIndex] == word[currentIndex - 1]:
                totalCount += 1

        return totalCount