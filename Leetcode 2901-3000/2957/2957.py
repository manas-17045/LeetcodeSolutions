# Leetcode 2957: Remove Adjacent Almost-Equal Characters
# https://leetcode.com/problems/remove-adjacent-almost-equal-characters/
# Solved on 5th of January, 2026
class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        """
        Calculates the minimum number of operations to remove all adjacent almost-equal characters.
        Two characters are considered almost-equal if their ASCII values differ by at most 1.
        An operation consists of changing a character to make it not almost-equal to its neighbor.

        Args:
            word (str): The input string.
        Returns:
            int: The minimum number of operations required.
        """
        operationsCount = 0
        currentIndex = 0
        wordLength = len(word)

        while currentIndex < wordLength - 1:
            if abs(ord(word[currentIndex]) - ord(word[currentIndex + 1])) <= 1:
                operationsCount += 1
                currentIndex += 2
            else:
                currentIndex += 1

        return operationsCount