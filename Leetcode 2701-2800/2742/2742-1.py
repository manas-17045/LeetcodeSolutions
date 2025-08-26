# Leetcode 2742: Painting the Walls
# https://leetcode.com/problems/painting-the-walls/
# Solved on 26th of August, 2025
class Solution:
    def paintWalls(self, cost: list[int], time: list[int]) -> int:
        """
        Calculates the minimum cost to paint all walls.

        Args:
            cost (list[int]): A list where cost[i] is the cost to paint the i-th wall.
            time (list[int]): A list where time[i] is the time taken to paint the i-th wall.
        Returns:
            int: The minimum cost to paint all walls.
        """

        n = len(cost)
        memo = {}

        def solve(index, wallsRemaining):
            if wallsRemaining <= 0:
                return 0

            if index == n:
                return float('inf')

            state = (index, wallsRemaining)
            if state in memo:
                return memo[state]

            paintCurrent = cost[index] + solve(index + 1, wallsRemaining - 1 - time[index])
            skipCurrent = solve(index + 1, wallsRemaining)

            result = min(paintCurrent, skipCurrent)
            memo[state] = result
            return result

        return solve(0, n)