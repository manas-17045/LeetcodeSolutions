# Leetcode 921: Minimum Add to Make Parentheses Valid
# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
# Solved on 6th of October, 2026
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        """
        Calculates the minimum number of parentheses insertions required to make the string valid.

        Parameters:
            s (str): The input parentheses string to evaluate.

        Returns:
            int: The minimum number of insertions required.
        """
        openCount = 0
        mismatchCount = 0

        for currentChar in s:
            if currentChar == '(':
                openCounr += 1
            elif openCount > 0:
                openCount -= 1
            else:
                mismatchCount += 1

        return openCount + mismatchCount