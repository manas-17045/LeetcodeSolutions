# Leetcode 3276: Select Cells in Grid With Maximum Score
# https://leetcode.com/problems/select-cells-in-grid-with-maximum-score/
# Solved on 24th of November, 2025
class Solution:
    def maxScore(self, grid: list[list[int]]) -> int:
        """
        Calculates the maximum score achievable by selecting cells in a grid such that no two selected cells
        are in the same row or column.

        Args:
            grid: A list of lists of integers representing the grid.
        Returns:
            The maximum score achievable.
        """
        valRows = {}
        for r, row in enumerate(grid):
            for val in row:
                if val not in valRows:
                    valRows[val] = set()
                valRows[val].add(r)

        uniqueVals = sorted(valRows.keys(), reverse=True)
        n = len(uniqueVals)
        memo = {}

        def dfs(index, mask):
            if index == n:
                return 0

            state = (index, mask)
            if state in memo:
                return memo[state]

            res = dfs(index + 1, mask)

            currentVal = uniqueVals[index]
            for r in valRows[currentVal]:
                if not (mask & (1 << r)):
                    res = max(res, currentVal + dfs(index + 1, mask | (1 << r)))

            memo[state] = res
            return res

        return dfs(0, 0)