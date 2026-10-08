// Leetcode 4046: Minimum Cost Path With At Most K Turns
// https://leetcode.com/problems/minimum-cost-path-with-at-most-k-turns/
// Solved on 8th of October, 2026
import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    /**
     * Calculates the minimum cost path from the top-left to the bottom-right of a grid 
     * with a maximum number of allowed turns.
     *
     * @param grid The 2D integer array representing the cost of visiting each cell.
     * @param k The maximum number of allowed turns.
     * @return The minimum path cost to reach the destination, or -1 if no such path exists.
     */
    public int minCost(nt[][] grid, int k) {
        int m = grid.length;
        int n = grid[0].length;
        if (m == 1 && n == 1) {
            return grid[0][0];
        }

        int[][][][] dist = new int[m][n][4][k + 1];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                for (int d = 0; d < 4; d++) {
                    java.util.Arrays.fill(dist[i][j][d], Integer.MAX_VALUE);
                }
            }
        }
        
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        int[] dr = {-1, 0, 1, 0};
        int[] dc = {0, 1, 0, -1};
        for (int i = 0; i < 4; i++) {
            int nr = dr[i];
            int nc = dc[i];
            if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                dist[nr][nc][i][0] = grid[0][0] + grid[nr][nc];
                pq.offer(new int[]{dist[nr][nc][i][0], nr, nc, i, 0});
            }
        }

        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int cost = curr[0];
            int r = curr[1];
            int c = curr[2];
            int dir = curr[3];
            int turns = curr[4];
            if (r == m - 1 && c == n - 1) {
                return cost;
            }

            if (cost > dist[r][c][dir][turns]) {
                continue;
            }

            for (int nextDir = 0; nextDir < 4; nextDir++) {
                int nr = r + dr[nextDir];
                int nc = c + dc[nextDir];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                    int nextTurns = turns + (dir != nextDir ? 1 : 0);
                    if (nextTurns <= k) {
                        int nextCost = cost + grid[nr][nc];
                        if (nextCost < dist[nr][nc][nextDir][nextTurns]) {
                            dist[nr][nc][nextDir][nextTurns] = nextCost;
                            pq.offer(new int[]{nextCost, nr, nc, nextDir, nextTurns});
                        }
                    }
                }
            }
        }
        return -1;
    }
}