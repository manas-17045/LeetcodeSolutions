# Leetcode 678: Valid Parenthsis String
# https://leetcode.com/problems/valid-parenthesis-string/
# Solved on 4th of October, 2026
class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        Determines whether the given string of parentheses and asterisks is valid.

        Parameters:
            s (str): The input string containing '(', ')', and '*'.

        Returns:
            bool: True if the string satisfies valid parenthesis rules, False otherwise.
        """
        minOpen = 0
        maxOpen = 0

        for currentChar in s:
            if currentChar == '(':
                minOpen += 1
                maxOpen += 1
            elif currentChar == ')':
                minOpen -= 1
                maxOpen -= 1
            else:
                minOpen -= 1
                maxOpen += 1

            if maxOpen < 0:
                return False

            if minOpen < 0:
                minOpen = 0

        return minOpen == 0