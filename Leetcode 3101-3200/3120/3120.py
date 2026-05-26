# Leetcode 3120: Count the Number of Special Characters I
# https://leetcode.com/problems/count-the-number-of-special-characters-i/
# Solved on 26th of May, 2026
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        """
        Counts the number of special characters in a string.
        A character is special if both its lowercase and uppercase forms appear in the string.

        :param word: The input string to check for special characters.
        :return: The total count of unique special characters.
        """
        lowerMask = 0
        upperMask = 0

        for currentLetter in word:
            if currentLetter.islower():
                lowerMask |= 1 << (ord(currentLetter) - 97)
            else:
                upperMask |= 1 << (ord(currentLetter) - 65)

        return bin(lowerMask & upperMask).count('1')