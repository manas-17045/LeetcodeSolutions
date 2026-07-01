// Leetcode 2812: Find the Safest Path in a Grid
// https://leetcode.com/problems/find-the-safest-path-in-a-grid/
// Solved on 1st of July, 2026
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;

class Solution {
    /**
     * Compute the maximum safeness factor of a path from (0, 0) to (n - 1, n - 1).
     * 
     * @param grid The grid representing the locations of thieves.
     * @return The maximum safeness factor of a path from (0, 0) to (n - 1, n - 1).
     */
    public int maximumSafenessFactor(List<List<Integer>> grid) {
        int n = grid.size();
        int[][] dist = new int[n][n];
        for (int[] row : dist) {
            Arrays.fill(row, -1);
        }
        
        Queue<int[]> queue = new ArrayDeque<>();
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                if (grid.get(r).get(c) == 1) {
                    queue.offer(new int[]{r, c});
                    dist[r][c] = 0;
                }
            }
        }
        
        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};
        
        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int r = curr[0];
            int c = curr[1];
            
            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i];
                int nc = c + dc[i];
                
                if (nr >= 0 && nr < n && nc >= 0 && nc < n && dist[nr][nc] == -1) {
                    dist[nr][nc] = dist[r][c] + 1;
                    queue.offer(new int[]{nr, nc});
                }
            }
        }
        
        PriorityQueue<int[]> maxHeap = new PriorityQueue<>((a, b) -> Integer.compare(b[0], a[0]));
        boolean[][] visited = new boolean[n][n];
        
        maxHeap.offer(new int[]{dist[0][0], 0, 0});
        visited[0][0] = true;
        
        while (!maxHeap.isEmpty()) {
            int[] curr = maxHeap.poll();
            int d = curr[0];
            int r = curr[1];
            int c = curr[2];
            
            if (r == n - 1 && c == n - 1) {
                return d;
            }
            
            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i];
                int nc = c + dc[i];
                
                if (nr >= 0 && nr < n && nc >= 0 && nc < n && !visited[nr][nc]) {
                    visited[nr][nc] = true;
                    maxHeap.offer(new int[]{Math.min(d, dist[nr][nc]), nr, nc});
                }
            }
        }
        
        return 0;
    }
}