// Leetcode 1970: Last Day Where You Can Still Cross
// https://leetcode.com/problems/last-day-where-you-can-still-cross/
// Solved on 31st of December, 2025
import java.util.ArrayDeque;
import java.util.Queue;

class Solution {
    /**
     * Finds the latest day you can still cross from the top row to the bottom row of a grid.
     *
     * @param row The number of rows in the grid.
     * @param col The number of columns in the grid.
     * @param cells A 2D array where `cells[i] = [r, c]` means that on day `i+1`, the cell `(r, c)` becomes water.
     * @return The latest day you can still cross from the top row to the bottom row.
     */
    public int latestDayToCross(int row, int col, int[][]cells) {
        int left = 1;
        int right = cells.length;
        int latestDay = 0;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (canCross(row, col, mid, cells)) {
                latestDay = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return latestDay;
    }

    private boolean canCross(int row, int col, int day, int[][] cells) {
        int[][] grid = new int[row][col];
        for (int i = 0; i < day; i++) {
            grid[cells[i][0] - 1][cells[i][1] - 1] = 1;
        }

        Queue<int[]> queue = new ArrayDeque<>();
        for (int c = 0; c < col; c++) {
            if (grid[0][c] == 0) {
                queue.offer(new int[]{0, c});
                grid[0][c] = 1;
            }
        }

        int[] dRow = {0, 0, 1, -1};
        int[] dCol = {1, -1, 0, 0};

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int r = current[0];
            int c = current[1];

            if (r == row - 1) {
                return true;
            }

            for (int i = 0; i < 4; i++) {
                int nr = r + dRow[i];
                int nc = c + dCol[i];

                if (nr >= 0 && nr < row && nc >= 0 && nc < col && grid[nr][nc] == 0) {
                    grid[nr][nc] = 1;
                    queue.offer(new int[]{nr, nc});
                }
            }
        }
        return false;
    }
}