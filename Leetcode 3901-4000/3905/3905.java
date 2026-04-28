// Leetcode 3905: Multi Source Flood Fill
// https://leetcode.com/problems/multi-source-flood-fill/
// Solved on 28th of April, 2026
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;

class Solution {
    /**
     * Performs a multi-source flood fill on an n x m grid.
     * 
     * @param n       The number of rows in the grid.
     * @param m       The number of columns in the grid.
     * @param sources A 2D array where each element is [row, col, color].
     * @return        The resulting grid after the flood fill operation.
     */
    public int[][] colorGrid(int n, int m, int[][] sources) {
        int[][] grid = new int[n][m];
        Arrays.sort(sources, (a, b) -> Integer.compare(b[2], a[2]));
        Queue<int[]> queue = new ArrayDeque<>();
        
        for (int[] source : sources) {
            int r = source[0];
            int c = source[1];
            int color = source[2];
            grid[r][c] = color;
            queue.offer(new int[]{r, c, color});
        }
        
        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};
        
        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int r = curr[0];
            int c = curr[1];
            int color = curr[2];
            
            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i];
                int nc = c + dc[i];
                
                if (nr >= 0 && nr < n && nc >= 0 && nc < m && grid[nr][nc] == 0) {
                    grid[nr][nc] = color;
                    queue.offer(new int[]{nr, nc, color});
                }
            }
        }
        
        return grid;
    }
}