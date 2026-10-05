# Leetcode 856: Score of Parentheses
# https://leetcode.com/problems/score-of-parentheses/
# Solved on 5th of October, 2026
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        """
        Calculates the score of a balanced parentheses string.

        Parameters:
            s (str): The balanced parentheses string.

        Returns:
            int: The total score computed according to the problem rules.
        """
        totalScore = 0
        currentDepth = 0

        for charIndex in range(len(s)):
            if s[charIndex] == '(':
                currentDepth += 1
            else:
                currentDepth -= 1
                if s[charIndex - 1] == '(':
                    totalScore += 1 << currentDepth

        return totalScore