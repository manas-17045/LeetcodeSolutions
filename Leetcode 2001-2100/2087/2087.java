// Leetcode 2087: Minimum Cost Homecoming of a Robot in a Grid
// https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/
// Solved on 1st of November, 2025
class Solution {
    /**
     * Calculates the minimum cost for a robot to travel from a starting position to a home position in a grid.
     * @param startPos An array of two integers representing the starting row and column [startRow, startCol].
     * @param homePos An array of two integers representing the home row and column [homeRow, homeCol].
     * @param rowCosts An array where rowCosts[i] is the cost to move to row i.
     * @param colCosts An array where colCosts[j] is the cost to move to column j.
     * @return The minimum total cost to reach the home position from the starting position.
     */
    public int minCost(int[] startPos, int[] homePos, int[] rowCosts, int[] colCosts) {
        int totalCost = 0;
        int startRow = startPos[0];
        int startCol = startPos[1];
        int homeRow = homePos[0];
        int homeCol = homePos[1];

        int currentRow = startRow;
        while (currentRow != homeRow) {
            if (currentRow < homeRow) {
                currentRow++;
            } else {
                currentRow--;
            }
            totalCost += rowCosts[currentRow];
        }

        int currentCol = startCol;
        while (currentCol != homeCol) {
            if (currentCol < homeCol) {
                currentCol++;
            } else {
                currentCol--;
            }
            totalCost += colCosts[currentCol];
        }

        return totalCost;
    }
}