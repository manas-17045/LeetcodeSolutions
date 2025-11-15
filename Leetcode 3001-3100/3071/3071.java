// Leetcode 3071: Minimum Operations to Write the Letter Y on a Grid
// https://leetcode.com/problems/minimum-operations-to-write-the-letter-y-on-a-grid/
// Solved on 14th of November, 2025
class Solution {
    /**
     * Calculates the minimum number of operations to write the letter 'Y' on a grid.
     * An operation consists of changing the value of a cell.
     * @param grid The input grid of integers.
     * @return The minimum number of operations required.
     */
    public int minimumOperationsToWriteY(int[][] grid) {
        int n = grid.length;
        int center = n / 2;
        int[] yCount = new int[3];
        int[] nonCount = new int[3];
        int totalY = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                boolean isY = (i <= center && (i == j || j == n - 1 - i)) || (i >= center && j == center);
                int v = grid[i][j];
                if (isY) {
                    yCount[v]++;
                    totalY++;
                } else {
                    nonCount[v]++;
                }
            }
        }
        int totalNon = n * n - totalY;
        int best = Integer.MAX_VALUE;
        for (int a = 0; a < 3; a++) {
            for (int b = 0; b < 3; b++) {
                if (a == b) {
                    continue;
                }
                int cost = (totalY - yCount[a]) + (totalNon - nonCount[b]);
                if (cost < best) {
                    best = cost;
                }
            }
        }
        return best;
    }
}