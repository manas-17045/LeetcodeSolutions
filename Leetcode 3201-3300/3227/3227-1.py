# Leetcode 3227: Vowels Game in a String
# https://leetcode.com/problems/vowels-game-in-a-string/
# Solved on 12th of September, 2025
class Solution:
    def doesAlicWin(self, s: str) -> bool:
        """
        Determines if Alice can win the Vowels Game.

        Args:
            s (str): The input string.
        Returns:
            bool: True if Alice can win, False otherwise.
        """
        vowelCount = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for char in s:
            if char in vowels:
                vowelCount += 1

        if vowelCount == 0:
            return False

        return True