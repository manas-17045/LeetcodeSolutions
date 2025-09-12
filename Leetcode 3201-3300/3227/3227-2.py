# Leetcode 3227: Vowels Game in a String
# https://leetcode.com/problems/vowels-game-in-a-string/
# Solved on 12th of September, 2025
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        """
        Determines if Alice wins based on the presence of vowels in the input string.
        :param s: The input string.
        :return: True if the string contains at least one vowel, False otherwise.
        """
        vowels = set("aeiou")
        for ch in s:
            if ch in vowels:
                return True

        return False