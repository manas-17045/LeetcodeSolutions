# Leetcode 1111: Maximum Nesting Depth of Two Valid Parentheses Strings
# https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/
# Solved on 12th of September, 2025
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        """
        Splits a valid parentheses string into two valid parentheses strings such that the maximum nesting depth of
        the two new strings is minimized.

        Args:
            seq (str): The input valid parentheses string.
        Returns:
            list[int]: A list of 0s and 1s, where 0 indicates the character belongs to the first string and 1 to the second.
        """
        answer = []
        depth = 0
        for char in seq:
            if char == '(':
                answer.append(depth % 2)
                depth += 1
            else:
                depth -= 1
                answer.append(depth % 2)

        return answer