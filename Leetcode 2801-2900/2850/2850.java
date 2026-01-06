// Leetcode 2850: Minimum Moves to Spread Stones Over Grid
// https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/
// Solved on 6th of January, 2026
class Solution {
    /**
     * Calculates the minimum number of moves required to spread stones over a 3x3 grid
     * such that each cell has exactly one stone.
     * A move consists of taking one stone from a cell with more than one stone
     * and moving it to an adjacent cell (up, down, left, or right).
     * @param grid The 3x3 grid representing the initial stone distribution.
     * @return The minimum number of moves.
     */
    public int minimumMoves(int[][] grid) {
        int zeroCount = 0;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (grid[i][j] == 0) {
                    zeroCount++;
                }
            }
        }
        if (zeroCount == 0) {
            return 0;
        }

        int minMoves = Integer.MAX_VALUE;

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (grid[i][j] == 0) {
                    for (int r = 0; r < 3; r++) {
                        for (int c = 0; c < 3; c++) {
                            if (grid[r][c] > 1) {
                                grid[r][c]--;
                                grid[i][j]++;
                                
                                int moves = Math.abs(r - i) + Math.abs(c - j);
                                int result = minimumMoves(grid);
                                minMoves = Math.min(minMoves, moves + result);

                                grid[r][c]++;
                                grid[i][j]--;
                            }
                        }
                    }
                    return minMoves;
                }
            }
        }
        return minMoves;
    }
}