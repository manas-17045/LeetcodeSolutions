# Leetcode 20: Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/
# Solved on 1st of October, 2026
class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determine if the input string containing brackets is valid.

        Parameters:
            s (str): The string containing bracket characters '()[]{}'.

        Returns:
            bool: True if the bracket sequence is valid, False otherwise.
        """
        if len(s) % 2 != 0:
            return False

        bracketMap = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        charStack = []

        for charToken in s:
            if charToken in bracketMap:
                if not charStack or charStack[-1] != bracketMap[charToken]:
                    return False
                charStack.pop()
            else:
                charStack.append(charToken)
        
        return not charStack