# Leetcode 848: Shifting Letters
# https://leetcode.com/problems/shifting-letters/
# Solved on 4th of July, 2025
class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        """
        Shifts letters in a string based on a list of shift values.

        The shifts are applied cumulatively from right to left.
        For example, shifts[i] applies to s[i] and all characters to its right.

        Args:
            s: The input string consisting of lowercase English letters.
            shifts: A list of integers representing the shift values.

        Returns:
            The modified string after applying all shifts.
        """
        numChars = len(s)
        resultChars = list(s)
        totalShift = 0

        for i in range((numChars - 1), -1, -1):
            totalShift += shifts[i]

            originalCode = ord(resultChars[i]) - ord('a')
            shiftedCode = (originalCode + totalShift) % 26

            resultChars[i] = chr(shiftedCode + ord('a'))

        return "".join(resultChars)