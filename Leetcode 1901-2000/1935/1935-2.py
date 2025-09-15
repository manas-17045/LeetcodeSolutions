# Leetcode 1935: Maximum Number of Words You Can Type
# https://leetcode.com/problems/maximum-number-of-words-you-can-type/
# Solved on 15th of September, 2025
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        """
        Calculates the number of words in a given text that can be typed,
        given a set of broken letters.
        :param text: The input string containing words separated by spaces.
        :param brokenLetters: A string containing all characters that are broken.
        :return: The number of words that can be typed.
        """
        # Build bitmask for broken letters
        mask = 0
        for c in brokenLetters:
            mask |= 1 << (ord(c) - ord('a'))

        count = 0
        for word in text.split():
            # Check if any character in the word is broken
            for ch in word:
                if (mask >> (ord(ch) - ord('a'))) & 1:
                    break
            else:
                # No broken character found in this word
                count += 1

        return count