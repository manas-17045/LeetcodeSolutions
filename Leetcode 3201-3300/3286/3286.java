// Leetcode 3286: Find a Safe Walk Through a Grid
// https://leetcode.com/problems/find-a-safe-walk-through-a-grid/
// Solved on 1st of December, 2025
import java.util.List;
import java.util.Deque;
import java.util.ArrayDeque;
import java.util.Arrays;

class Solution {
    /**
     * Finds if there is a safe walk from the top-left corner (0,0) to the bottom-right corner (m-1, n-1)
     * of a grid, given a starting health. A walk is safe if the accumulated cost (sum of grid values)
     * never reaches or exceeds the initial health.
     * @param grid The input grid where each cell contains a cost.
     * @param health The initial health.
     * @return True if a safe walk exists, false otherwise.
     */
    public boolean findSafeWalk(List<List<Integer>> grid, int health) {
        int m = grid.size();
        int n = grid.get(0).size();
        
        int[][] dist = new int[m][n];
        for (int[] row : dist) {
            Arrays.fill(row, Integer.MAX_VALUE);
        }
        
        Deque<int[]> deque = new ArrayDeque<>();
        int startCost = grid.get(0).get(0);
        
        if (startCost >= health) {
            return false;
        }
        
        dist[0][0] = startCost;
        deque.offerFirst(new int[]{0, 0});
        
        int[] dr = {0, 0, 1, -1};
        int[] dc = {1, -1, 0, 0};
        
        while (!deque.isEmpty()) {
            int[] current = deque.pollFirst();
            int r = current[0];
            int c = current[1];
            
            if (r == m - 1 && c == n - 1) {
                return true;
            }
            
            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i];
                int nc = c + dc[i];
                
                if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                    int weight = grid.get(nr).get(nc);
                    int newDist = dist[r][c] + weight;
                    
                    if (newDist < health && newDist < dist[nr][nc]) {
                        dist[nr][nc] = newDist;
                        if (weight == 0) {
                            deque.offerFirst(new int[]{nr, nc});
                        } else {
                            deque.offerLast(new int[]{nr, nc});
                        }
                    }
                }
            }
        }
        
        return false;
    }
}