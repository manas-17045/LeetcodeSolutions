# Leetcode 3361: Shift Distance Between Two Strings
# https://leetcode.com/problems/shift-distance-between-two-strings/
# Solved on 4th of July, 2025
class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: list[int], previousCost: list[int]) -> int:
        """
        Calculates the minimum total cost to transform string s into string t
        by shifting each character individually.

        The cost of shifting a character 'c' to 'c+1' is given by nextCost[c - 'a'],
        and the cost of shifting 'c' to 'c-1' is given by previousCost[c - 'a'].
        The shifts wrap around (e.g., 'z' + 1 = 'a', 'a' - 1 = 'z').

        Args:
            s: The source string.
            t: The target string.
            nextCost: A list of integers where nextCost[i] is the cost to shift 'a'+i to 'a'+i+1.
            previousCost: A list of integers where previousCost[i] is the cost to shift 'a'+i to 'a'+i-1.

        Returns:
            The minimum total cost to transform s into t.
        """
        numChars = 26
        infinity = float('inf')

        minCosts = [[infinity] * numChars for _ in range(numChars)]

        for i in range(numChars):
            minCosts[i][i] = 0

        for i in range(numChars):
            nextCharIndex = (i + 1) % numChars
            minCosts[i][nextCharIndex] = min(minCosts[i][nextCharIndex], nextCost[i])

            prevCharIndex = (i - 1 + numChars) % numChars
            minCosts[i][prevCharIndex] = min(minCosts[i][prevCharIndex], previousCost[i])

        for k in range(numChars):
            for i in range(numChars):
                for j in range(numChars):
                    if minCosts[i][k] != infinity and minCosts[k][j] != infinity:
                        minCosts[i][j] = min(minCosts[i][j], minCosts[i][k] + minCosts[k][j])

        totalCost = 0
        for i in range(len(s)):
            startCharIndex = ord(s[i]) - ord('a')
            endCharIndex = ord(t[i]) - ord('a')
            cost = minCosts[startCharIndex][endCharIndex]
            totalCost += cost

        return int(totalCost)