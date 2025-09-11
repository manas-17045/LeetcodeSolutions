# Leetcode 1444: Number of Ways of Cutting a Pizza
# https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/
# Solved on 11th of September, 2025
class Solution:
    def ways(self, pizza: list[str], k: int) -> int:
        """
        Calculates the number of ways to cut a pizza into k pieces such that each piece has at least one apple.

        Args:
            pizza (list[str]): A list of strings representing the pizza, where 'A' denotes an apple and '.' denotes an empty cell.
            k (int): The number of pieces to cut the pizza into.
        Returns:
            int: The number of ways to cut the pizza, modulo 10^9 + 7.
        """
        numRows = len(pizza)
        numCols = len(pizza[0])
        mod = 10**9 + 7

        apples = [[0] * (numCols + 1) for _ in range(numRows + 1)]
        for row in range(numRows - 1, -1, -1):
            for col in range(numCols - 1, -1, -1):
                hasApple = 1 if pizza[row][col] == 'A' else 0
                apples[row][col] = (hasApple +
                                    apples[row + 1][col] +
                                    apples[row][col + 1] -
                                    apples[row + 1][col + 1]
                                    )

        memo = {}

        def solve(row, col, pieces):
            state = (row, col, pieces)
            if state in memo:
                return memo[state]

            if apples[row][col] < pieces:
                memo[state] = 0
                return 0

            if pieces == 1:
                memo[state] = 1
                return 1

            numWays = 0

            for nextRow in range(row + 1, numRows):
                if apples[row][col] > apples[nextRow][col]:
                    numWays = (numWays + solve(nextRow, col, pieces - 1)) % mod

            for nextCol in range(col + 1, numCols):
                if apples[row][col] > apples[row][nextCol]:
                    numWays = (numWays + solve(row, nextCol, pieces - 1)) % mod

            memo[state] = numWays
            return numWays

        return solve(0, 0, k)