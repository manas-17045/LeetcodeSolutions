// Leetcode 1293: Shortest Path in a Grid with Obstacles Elimination
// https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
// Solved on 1st of December, 2025
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

class Solution {
    /**
     * Finds the shortest path from the top-left corner (0,0) to the bottom-right corner (m-1, n-1)
     * of a grid, allowing to eliminate at most 'k' obstacles.
     * @param grid The input grid where 0 represents an empty cell and 1 represents an obstacle.
     * @param k The maximum number of obstacles that can be eliminated.
     * @return The length of the shortest path, or -1 if no such path exists.
     */
    public int shortestPath(int[][] grid, int k) {
        int m = grid.length;
        int n = grid[0].length;
        if (k >= m + n - 2) {
            return m + n - 2;
        }
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{0, 0, k});
        int[][] visited = new int[m][n];
        for (int[] row : visited) {
            Arrays.fill(row, -1);
        }
        visited[0][0] = k;
        int steps = 0;
        int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        while (!queue.isEmpty()) {
            int size = queue.size();
            while (size-- > 0) {
                int[] current = queue.poll();
                int row = current[0];
                int col = current[1];
                int currentK = current[2];
                if (row == m - 1 && col == n - 1) {
                    return steps;
                }
                for (int[] dir : directions) {
                    int nextRow = row + dir[0];
                    int nextCol = col + dir[1];
                    if (nextRow >= 0 && nextRow < m && nextCol >= 0 && nextCol < n) {
                        int nextK = currentK - grid[nextRow][nextCol];
                        if (nextK >= 0 && nextK > visited[nextRow][nextCol]) {
                            visited[nextRow][nextCol] = nextK;
                            queue.offer(new int[]{nextRow, nextCol, nextK});
                        }
                    }
                }
            }
            steps++;
        }
        return -1;
    }
}