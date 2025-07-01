# Leetcode 917: Reverse Only Letters
# https://leetcode.com/problems/reverse-only-letters/
# Solved on 1st of July, 2025
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        """
        Reverses only the letter characters in a given string,
        leaving non-letter characters in their original positions.

        Args:
            s: The input string.
        Returns:
            The string with only letters reversed.
        """
        sChars = list(s)
        leftPointer = 0
        rightPointer = len(s) - 1

        while leftPointer < rightPointer:
            if not sChars[leftPointer].isalpha():
                leftPointer += 1
            elif not sChars[rightPointer].isalpha():
                rightPointer -= 1
            else:
                sChars[leftPointer], sChars[rightPointer] = sChars[rightPointer], sChars[leftPointer]
                leftPointer += 1
                rightPointer -= 1

        return "".join(sChars)