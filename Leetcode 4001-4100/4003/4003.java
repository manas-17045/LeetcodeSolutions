// Leetcode 4003: Minimum Cost Path with Alternating Directions III
// https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-iii/
// Solved on 26th of August, 2026
import java.util.Arrays;
import java.util.PriorityQueue;

class Solution {
    /**
     * Calculates the minimum cost to reach the bottom-right corner of a grid starting from the top-left corner.
     * The cost depends on movement directions and an alternating parity rule, where waiting or violating the
     * parity rule incurs a penalty cost based on the current cell.
     *
     * @param m       the number of rows in the grid
     * @param n       the number of columns in the grid
     * @param penalty a 2D integer array representing the penalty cost at each cell
     * @return the minimum total cost to reach cell (m - 1, n - 1)
     */
    public long minCost(int m, int n, nt[][] penalty) {
        long[][] dist = new long[m * n][2];
        for (int i = 0; i < m * n; i++) {
            Arrays.fill(dist[i], Long.MAX_VALUE);
        }
        dist[0][1] = 1;

        PriorityQueue<long[]> pq = new PriorityQueue<>((a, b) -> Long.compare(a[0], b[0]));
        pq.offer(new long[]{1, 0, 0, 1});

        int[] dr = {0, 1, 0, -1};
        int[] dc = {1, 0, -1, 0};

        while (!pq.isEmpty()) {
            long[] curr = pq.poll();
            long currCost = curr[0];
            int r = (int) curr[1];
            int c = (int) curr[2];
            int parity = (int) curr[3];

            if (currCost > dist[r * n + c][parity]) {
                continue;
            }

            if (r == m - 1 && c == n - 1) {
                return currCost;
            }

            long waitCost = currCost + penalty[r][c];
            int nextParity = 1 - parity;
            if (waitCost < dist[r * n + c][nextParity]) {
                dist[r * n + c][nextParity] = waitCost;
                pq.offer(new long[]{waitCost, r, c, nextParity});
            }

            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i];
                int nc = c + dc[i];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                    long moveCost = currCost + (long) (nr + 1) * (nc + 1);
                    int requiredParity = (i < 2) ? 1 : 0;
                    if (parity != requiredParity) {
                        moveCost += penalty[r][c];
                    }
                    if (moveCost < dist[nr * n + nc][nextParity]) {
                        dist[nr * n + nc][nextParity] = moveCost;
                        pq.offer(new long[]{moveCost, nr, nc, nextParity});
                    }
                }
            }
        }
        
        return -1;
    }
}