# Leetcode 2087: Minimum Cost Homecoming of a Robot in a Grid
# https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/
# Solved on 1st of November, 2025
class Solution:
    def minCost(self, startPos: list[int], homePos: list[int], rowCosts: list[int], colCosts: list[int]) -> int:
        """
        Calculates the minimum cost for a robot to travel from a starting position to a home position in a grid.
        The cost of moving between adjacent cells in a row or column is given by `rowCosts` and `colCosts` respectively.

        Args:
            startPos (list[int]): A list of two integers [start_row, start_col] representing the robot's starting position.
            homePos (list[int]): A list of two integers [home_row, home_col] representing the robot's home position.
            rowCosts (list[int]): A list of integers where rowCosts[i] is the cost of moving to row i.
            colCosts (list[int]): A list of integers where colCosts[j] is the cost of moving to column j.

        Returns:
            int: The minimum total cost to reach the home position.
        """
        totalCost = 0
        startRow = startPos[0]
        startCol = startPos[1]
        homeRow = homePos[0]
        homeCol = homePos[1]

        currentRow = startRow
        while currentRow != homeRow:
            if currentRow < homeRow:
                currentRow += 1
            else:
                currentRow -= 1
            totalCost += rowCosts[currentRow]

        currentCol = startCol
        while currentCol != homeCol:
            if currentCol < homeCol:
                currentCol += 1
            else:
                currentCol -= 1
            totalCost += colCosts[currentCol]

        return totalCost