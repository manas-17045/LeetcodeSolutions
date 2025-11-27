// Leetcode 3619: Count Islands With Total Value Divisible by K
// https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/
// Solved on 27th of November, 2025
import java.util.ArrayDeque;
import java.util.Queue;

class Solution {
    /**
     * Counts the number of islands in a grid where the sum of values in each island is divisible by k.
     * An island is a group of connected cells with positive values. Cells are connected horizontally or vertically.
     *
     * @param grid The input grid where positive values represent land and 0 represents water.
     * @param k The divisor to check for the sum of island values.
     * @return The total count of islands whose sum of values is divisible by k.
     */
    public int countIslands(int[][] grid, int k) {
        int rows = grid.length;
        int cols = grid[0].length;
        int count = 0;
        int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] > 0) {
                    long currentSum = 0;
                    Queue<int[]> queue = new ArrayDeque<>();
                    queue.offer(new int[]{i, j});
                    currentSum += grid[i][j];
                    grid[i][j] = 0;

                    while (!queue.isEmpty()) {
                        int[] current = queue.poll();
                        int r = current[0];
                        int c = current[1];

                        for (int[] dir : directions) {
                            int nr = r + dir[0];
                            int nc = c + dir[1];

                            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] > 0) {
                                currentSum += grid[nr][nc];
                                grid[nr][nc] = 0;
                                queue.offer(new int[]{nr, nc});
                            }
                        }
                    }

                    if (currentSum % k == 0) {
                        count++;
                    }
                }
            }
        }
        return count;
    }
}