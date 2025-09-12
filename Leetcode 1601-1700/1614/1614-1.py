# Leetcode 1614: Maximum Nesting Depth of the Parentheses
# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
# Solved on 12th of September, 2025
class Solution:
    def maxDepth(self, s: str) -> int:
        """
        Calculates the maximum nesting depth of parentheses in a given string.

        Args:
            s (str): The input string containing parentheses.
        Returns:
            int: The maximum nesting depth of parentheses.
        """
        maxDepth = 0
        currentDepth = 0

        for character in s:
            if character == '(':
                currentDepth += 1
                if currentDepth > maxDepth:
                    maxDepth = currentDepth
            elif character == ')':
                currentDepth -= 1

        return maxDepth