# Leetcode 3136: Valid Word
# https://leetcode.com/problems/valid-word/
# Solved on 15th of July, 2025
class Solution:
    def isValid(self, word: str) -> bool:
        """
        Checks if a given word is valid according to specific rules.

        Args:
            word (str): The input word to validate.
        Returns:
            bool: True if the word is valid, False otherwise.
        """
        wordLength = len(word)
        if wordLength < 3:
            return False

        hasVowel = False
        hasConsonant = False
        vowels = "aeiouAEIOU"

        for char in word:
            isLetter = char.isalpha()
            isDigit = char.isdigit()

            if not isLetter and not isDigit:
                return False

            if isLetter:
                if char in vowels:
                    hasVowel = True
                else:
                    hasConsonant = True

        return hasVowel and hasConsonant