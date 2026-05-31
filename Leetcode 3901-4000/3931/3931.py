# Leetcode 3931: Check Adjacent Digit Differences
# https://leetcode.com/problems/check-adjacent-digit-differences/
# Solved on 31st of May, 2026
class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        """
        Checks if the absolute difference between every pair of adjacent digits in the string is at most 2.

        Args:
            s (str): A string consisting of numeric digits.
        Returns:
            bool: True if all adjacent digit differences are <= 2, False otherwise.
        """
        for loopIndex in range(len(s) - 1):
            currentDigit = int(s[loopIndex])
            nextDigit = int(s[loopIndex + 1])

            if abs(currentDigit - nextDigit) > 2:
                return False

        return True