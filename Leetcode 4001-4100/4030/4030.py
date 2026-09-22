# Leetcode 4030: Check ASCII Palindromic
# https://leetcode.com/problems/check-ascii-palindromic/
# Solved on 22nd of September, 2026
class Solution:
    def isPalindromic(self, s: str) -> bool:
        """
        Checks if the concatenated 8-bit binary representation of the string is palindromic.

        Args:
            s (str): The input string consisting of lowercase English letters.

        Returns:
            bool: True if the resulting binary string is a palindrome, False otherwise.
        """
        leftIndex = 0
        rightIndex = len(s) - 1

        while leftIndex <= rightIndex:
            leftVal = ord(s[leftIndex])
            rightVal = ord(s[rightIndex])

            for bitIndex in range(8):
                if ((leftVal >> bitIndex) & 1) != ((rightVal >> (7 - bitIndex)) & 1):
                    return False

            leftIndex += 1
            rightIndex += 1

        return True