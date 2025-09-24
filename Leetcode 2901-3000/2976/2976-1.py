# Leetcode 2976: Minimum Cost to Convert String I
# https://leetcode.com/problems/minimum-cost-to-convert-string-i/
# Solved on 24th of September, 2025
class Solution:
    def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        """
        Calculates the minimum cost to convert the source string to the target string.

        Args:
            source (str): The original string.
            target (str): The target string to convert to.
            original (list[str]): A list of characters that can be changed.
            changed (list[str]): A list of characters that original[i] can be changed to.
            cost (list[int]): The cost of changing original[i] to changed[i].

        Returns:
            int: The minimum cost to convert source to target. Returns -1 if it's impossible
                 to convert.
        """
        numChars = 26
        infinity = float('inf')

        minCostMatrix = [[infinity] * numChars for _ in range(numChars)]

        for i in range(numChars):
            minCostMatrix[i][i] = 0

        for i in range(len(original)):
            fromCharIndex = ord(original[i]) - ord('a')
            toCharIndex = ord(changed[i]) - ord('a')
            conversionCost = cost[i]
            minCostMatrix[fromCharIndex][toCharIndex] = min(minCostMatrix[fromCharIndex][toCharIndex], conversionCost)

        for k in range(numChars):
            for i in range(numChars):
                for j in range(numChars):
                    if minCostMatrix[i][k] != infinity and minCostMatrix[k][j] != infinity:
                        minCostMatrix[i][j] = min(minCostMatrix[i][j], minCostMatrix[i][k] + minCostMatrix[k][j])

        totalCost = 0
        for i in range(len(source)):
            sourceCharIndex = ord(source[i]) - ord('a')
            targetCharIndex = ord(target[i]) - ord('a')

            conversionCost = minCostMatrix[sourceCharIndex][targetCharIndex]

            if conversionCost == infinity:
                return -1

            totalCost += conversionCost

        return int(totalCost)