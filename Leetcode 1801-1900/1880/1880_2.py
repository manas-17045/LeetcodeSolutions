# Leetcode 1880: Check if Word Equals Summation of Two Words
# https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/
# Solved on 2nd of August, 2025
class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        """
        Checks if the sum of the numerical values of two words equals the numerical value of a third word.
        Each letter 'a' through 'j' corresponds to a digit 0 through 9.
        :param firstWord: The first word (string of lowercase English letters 'a'-'j').
        :param secondWord: The second word (string of lowercase English letters 'a'-'j').
        :param targetWord: The target word (string of lowercase English letters 'a'-'j').
        :return: True if ``word_value(firstWord) + word_value(secondWord) == word_value(targetWord)``, False otherwise.
        """
        def word_value(w: str) -> int:
            v = 0
            for c in w:
                # Letter 'a' -> 0, 'b' -> 1, ..., 'j' -> 9
                v = v * 10 + (ord(c) - ord('a'))
            return v
        
        return word_value(firstWord) + word_value(secondWord) == word_value(targetWord)