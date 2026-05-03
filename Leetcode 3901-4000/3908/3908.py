# Leetcode 3908: Valid Digit Number
# https://leetcode.com/problems/valid-digit-number/
# Solved on 3rd of May, 2026
class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        """
        Checks if the number n contains the digit x, but does not start with it.

        :param n: The integer to be checked.
        :param x: The digit to look for within n.
        :return: True if n contains x and the first digit of n is not x, False otherwise.
        """
        if n == 0:
            return False

        containsDigit = False
        firstDigit = 0
        tempNumber = n

        while tempNumber > 0:
            firstDigit = tempNumber % 10
            if firstDigit == x:
                containsDigit = True
            tempNumber //= 10

        return containsDigit and firstDigit != x