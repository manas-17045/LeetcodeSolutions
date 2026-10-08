# Leetcode 1021: Remove Outermost Parentheses
# https://leetcode.com/problems/remove-outermost-parentheses/
# Solved on 8th of October, 2026
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        """
        Decomposes a valid parentheses string into primitive components and returns the string with all outermost parentheses removed.

        Parameters:
            s (str): A valid parentheses string.

        Returns:
            str: The string after stripping the outermost parentheses of each primitive block.
        """
        resultParts = []
        openCount = 0

        for currentChar in s:
            if currentChar == "(":
                if openCount > 0:
                    resultParts.append(currentChar)
                openCount += 1
            else:
                openCount -= 1
                if openCount > 0:
                    resultParts.append(currentChar)
        
        return "".join(resultParts)