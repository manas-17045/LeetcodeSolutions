# Leetcode 2423: Remove Letter To Equalize Frequency
# https://leetcode.com/problems/remove-letter-to-equalize-frequency/
# Solved on 21st of August, 2025
from collections import Counter


class Solution:
    def equalFrequency(self, word: str) -> bool:
        """
        Checks if it's possible to make all character frequencies equal by removing exactly one character.

        Args:
            word (str): The input string.
        Returns:
            bool: True if it's possible, False otherwise.
        """
        freq = Counter(word)
        for c in list(freq.keys()):
            freq[c] -= 1
            vals = [freq[x] for x in freq if freq[x] > 0]
            if len(set(vals)) == 1:
                return True
            freq[c] += 1
        return False