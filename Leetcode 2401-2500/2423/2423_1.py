# Leetcode 2423: Remove Letter To Equalize Frequency
# https://leetcode.com/problems/remove-letter-to-equalize-frequency/
# Solved on 21st of August, 2025
import collections


class Solution:
    def equalFrequency(self, word: str) -> bool:
        """
        Checks if it's possible to make all character frequencies equal by removing exactly one character.

        Args:
            word (str): The input string.
        Returns:
            bool: True if it's possible, False otherwise.
        """
        wordLength = len(word)
        for i in range(wordLength):
            tempWord = word[:i] + word[i + 1:]
            frequencyCounter = collections.Counter(tempWord)

            if not frequencyCounter:
                return True

            frequencyValues = set(frequencyCounter.values())

            if len(frequencyValues) == 1:
                return True

        return False