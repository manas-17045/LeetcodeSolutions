# Leetcode 32: Longest Valid Parentheses
# https://leetcode.com/problems/longest-valid-parentheses/
# Solved on 3rd of October, 2026
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        Computes the length of the longest valid parentheses substring.

        Parameters:
            s (str): The input string containing '(' and ')' characters.

        Returns:
            int: The maximum length of a valid parentheses substring.
        """
        maxLength = 0
        leftCount = 0
        rightCount = 0

        for bracketChar in s:
            if bracketChar == "(":
                leftCount += 1
            else:
                rightCount += 1

            if leftCount == rightCount:
                maxLength = max(maxLength, 2 * rightCount)
            elif rightCount > leftCount:
                leftCount = 0
                rightCount = 0

        leftCount = 0
        rightCount = 0

        for bracketChar in reversed(s):
            if bracketChar == "(":
                leftCount += 1
            else:
                rightCount += 1

            if leftCount == rightCount:
                maxLength = max(maxLength, 2 * leftCount)
            elif leftCount > rightCount:
                leftCount = 0
                rightCount = 0

        return maxLength