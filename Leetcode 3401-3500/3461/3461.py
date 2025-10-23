# Leetcode 3461: Check If Digits Are Equal in String After Operations I
# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/
# Solved on 23rd of October, 2025
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        """
        This function checks if, after a series of operations, the last two remaining digits in a string are equal.
        The operations involve repeatedly replacing adjacent digits with their sum modulo 10, and then removing the last digit.

        Args:
            s (str): A string consisting of digits.

        Returns:
            bool: True if the last two remaining digits are equal, False otherwise.
        """
        currentDigits = [int(digit) for digit in s]

        numDigits = len(currentDigits)

        while numDigits > 2:
            for i in range(numDigits - 1):
                currentDigits[i] = (currentDigits[i] + currentDigits[i + 1]) % 10

            currentDigits.pop()
            numDigits -= 1

        return currentDigits[0] == currentDigits[1]