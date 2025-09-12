# Leetcode 1111: Maximum Nesting Depth of Two Valid Parentheses Strings
# https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/
# Solved on 12th of September, 2025
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        """
        Splits a valid parentheses string into two valid parentheses strings such that the maximum depth of the two new strings is minimized.
        :param seq: The input valid parentheses string.
        :return: A list of integers where each element is 0 or 1, indicating which of the two new strings the corresponding parenthesis belongs to.
        """
        ans: list[int] = []
        depth = 0
        for ch in seq:
            if ch == '(':
                depth += 1
                # Assign based on parity after increment
                ans.append(depth & 1)
            else:
                # Assign based on parity before decrement
                ans.append(depth & 1)
                depth -= 1

        return ans