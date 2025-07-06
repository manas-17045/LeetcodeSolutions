# Leetcode 1473: Paint House III
# https://leetcode.com/problems/paint-house-iii/
# Solved on 6th of July, 2025
class Solution:
    def minCost(self, houses: list[int], cost: list[list[int]], m: int, n: int, target: int) -> int:
        """
        Calculates the minimum cost to paint all houses such that there are exactly `target` neighborhoods.

        Args:
            houses: A list of integers where houses[i] is the color of the i-th house (0 if unpainted).
            cost: A 2D list where cost[i][j] is the cost to paint house i with color j+1.
            m: The number of houses.
            n: The number of colors.
            target: The target number of neighborhoods.

        Returns:
            The minimum cost to paint all houses, or -1 if it's impossible to achieve the target number of neighborhoods.

        This problem is solved using dynamic programming.
        """
        infinity = float('inf')
        prevDp = [[infinity] * n for _ in range(target + 1)]

        if houses[0] == 0:
            for color in range(n):
                prevDp[1][color] = cost[0][color]
        else:
            colorIdx = houses[0] - 1
            prevDp[1][colorIdx] = 0

        for i in range(1, m):
            currentDp = [[infinity] * n for _ in range(target + 1)]

            maxNeighborhoods = min(target, (i + 1))
            for neighborhoods in range(1, (maxNeighborhoods + 1)):
                min1 = infinity
                idx1 = -1
                min2 = infinity

                for prevColor in range(n):
                    c = prevDp[neighborhoods - 1][prevColor]
                    if c < min1:
                        min2 = min1
                        min1 = c
                        idx1 = prevColor
                    elif c < min2:
                        min2 = c

                for color in range(n):
                    if houses[i] != 0 and houses[i] - 1 != color:
                        continue

                    paintCost = 0
                    if houses[i] == 0:
                        paintCost = cost[i][color]

                    sameColorCost = prevDp[neighborhoods][color]

                    diffColorCost = min1
                    if color == idx1:
                        diffColorCost = min2

                    prevMin = min(sameColorCost, diffColorCost)

                    if prevMin != infinity:
                        currentDp[neighborhoods][color] = prevMin + paintCost

            prevDp = currentDp

        result = min(prevDp[target])

        if result == infinity:
            return -1
        else:
            return int(result)