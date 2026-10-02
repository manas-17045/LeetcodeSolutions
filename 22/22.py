# Leetcode 22: Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/
# Solved on 2nd of October, 2026
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        """
        Generate all valid parentheses combinations using backtracking.

        Parameters:
            n (int): The number of pairs of parentheses.

        Returns:
            list[str]: A list containing all valid combinations.
        """
        validCombinations = []
        currentSequence = []

        def backtrack(openCount: int, closeCount: int) -> None:
            if len(currentSequence) == 2 * n:
                validCombinations.append("".join(currentSequence))
                return

            if openCount < n:
                currentSequence.append("(")
                backtrack(openCount + 1, closeCount)
                currentSequence.pop()

            if closeCount < openCount:
                currentSequence.append(")")
                backtrack(openCount, closeCount + 1)
                currentSequence.pop()

        backtrack(0, 0)
        return validCombinations