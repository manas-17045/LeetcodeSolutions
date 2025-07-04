# Leetcode 848: Shifting Letters
# https://leetcode.com/problems/shifting-letters/
# Solved on 4th of July, 2025
class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        """
        Applies a series of shifting operations to a string.

        Each `shifts[i]` indicates how much `s[i]` and all characters to its right
        should be shifted. The shifts are cumulative.

        Args:
            s (str): The input string consisting of lowercase English letters.
            shifts (list[int]): A list of integers representing the shift amounts.
                                shifts[i] is the shift for s[i] and all characters
                                to its right.

        Returns:
            str: The final string after all shifts have been applied.
        """
        n = len(s)
        res = [''] * n
        total_shift = 0

        # Traverse from right to left, accumulating shifts
        for i in range((n - 1), -1, -1):
            total_shift = (total_shift + shifts[i]) % 26
            # Original letter index 0-25
            alpha_index = ord(s[i]) - ord('a')
            # Apply shift
            new_index = (alpha_index + total_shift) % 26
            res[i] = chr(new_index + ord('a'))

        return ''.join(res)