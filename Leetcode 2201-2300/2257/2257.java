// Leetcode 2257: Count Unguarded Cells in the Grid
// https://leetcode.com/problems/count-unguarded-cells-in-the-grid/
// Solved on 2nd of November, 2025
class Solution {
    /**
     * Counts the number of unguarded cells in a grid.
     * @param m The number of rows in the grid.
     * @param n The number of columns in the grid.
     * @param guards An array of [row, col] pairs representing the positions of guards.
     * @param walls An array of [row, col] pairs representing the positions of walls.
     * @return The total count of unguarded cells.
     */
    public int countUnguarded(int m, int n, int[][] guards, int[][] walls) {
        final int EMPTY = 0;
        final int WALL = 1;
        final int GUARD = 2;
        final int GUARDED = 3;

        int[][] grid = new int[m][n];

        for (int[] wall : walls) {
            grid[wall[0]][wall[1]] = WALL;
        }

        for (int[] guard : guards) {
            grid[guard[0]][guard[1]] = GUARD;
        }

        for (int r = 0; r < m; r++) {
            boolean inSight = false;
            for (int c = 0; c < n; c++) {
                int state = grid[r][c];
                if (state == WALL || state == GUARD) {
                    inSight = (state == GUARD);
                } else if (state == EMPTY && inSight) {
                    grid[r][c] = GUARDED;
                }
            }

            inSight = false;
            for (int c = n - 1; c >= 0; c--) {
                int state = grid[r][c];
                if (state == WALL || state == GUARD) {
                    inSight = (state == GUARD);
                } else if (state == EMPTY && inSight) {
                    grid[r][c] = GUARDED;
                }
            }
        }

        for (int c = 0; c < n; c++) {
            boolean inSight = false;
            for (int r = 0; r < m; r++) {
                int state = grid[r][c];
                if (state == WALL || state == GUARD) {
                    inSight = (state == GUARD);
                } else if (state == EMPTY && inSight) {
                    grid[r][c] = GUARDED;
                }
            }

            inSight = false;
            for (int r = m - 1; r >= 0; r--) {
                int state = grid[r][c];
                if (state == WALL || state == GUARD) {
                    inSight = (state == GUARD);
                } else if (state == EMPTY && inSight) {
                    grid[r][c] = GUARDED;
                }
            }
        }

        int unguardedCount = 0;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == EMPTY) {
                    unguardedCount++;
                }
            }
        }

        return unguardedCount;
    })
}