# Leetcode 3856: Trim Trailing Vowels
# https://leetcode.com/problems/trim-trailing-vowels/
# Solved on 1st of March, 2026
class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        """
        Removes all consecutive vowel characters from the end of the string.

        :param s: The input string to be trimmed.
        :return: The resulting string after removing trailing vowels.
        """
        vowelSet = {'a', 'e', 'i', 'o', 'u'}
        endIndex = len(s) - 1

        while endIndex >= 0 and s[endIndex] in vowelSet:
            endIndex -= 1

        return s[:endIndex + 1]