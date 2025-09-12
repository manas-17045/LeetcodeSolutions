# Leetcode 1614: Maximum Nesting Depth of the Parentheses
# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
# Solved on 12th of September, 2025
class Solution:
    def maxDepth(self, s: str) -> int:
        """
        Calculates the maximum nesting depth of parentheses in a given string.
        :param s: The input string containing parentheses.
        :return: The maximum depth of nested parentheses.
        """
        cur = 0
        max_depth = 0
        for ch in s:
            if ch == '(':
                cur += 1
                if cur > max_depth:
                    max_depth = cur

            elif ch == ')':
                cur -= 1

        return max_depth