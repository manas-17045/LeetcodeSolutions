# Leetcode 3136: Valid Word
# https://leetcode.com/problems/valid-word/
# Solved on 15th of July, 2025
class Solution:
    def isValid(self, word: str) -> bool:
        """
        Checks if a given word is valid according to specific rules.

        A word is considered valid if:
        1. It has a length of at least 3.
        2. It consists only of English letters (lowercase and uppercase) and digits.
        3. It contains at least one vowel (a, e, i, o, u, A, E, I, O, U).
        4. It contains at least one consonant.

        Args:
            word (str): The word to be validated.

        Returns:
            bool: True if the word is valid, False otherwise.
        """
        # Length Check
        if len(word) < 3:
            return False

        # Prepare vowel set for quick lookup
        vowels = set("aeiouAEIOU")

        has_vowel = False
        has_consonant = False

        for ch in word:
            # Reject any non-letter, non-digit character
            if not (ch.isalpha() or ch.isdigit()):
                return False

            # If it's a letter, classify it
            if ch.isalpha():
                if ch in vowels:
                    has_vowel = True
                else:
                    has_consonant = True

            # Early exit if both are satisfied
            if has_vowel and has_consonant:
                continue

        # Final check: at least one vowel amd one consonant
        return has_vowel and has_consonant