// Leetcode 3651: Minimum Cost Path with Teleportations
// https://leetcode.com/problems/minimum-cost-path-with-teleportations/
// Solved on 2nd of December, 2025
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.PriorityQueue;

class Solution {
    /**
     * Calculates the minimum cost to reach the bottom-right corner of a grid with teleportations.
     *
     * @param grid The input grid where each cell contains a cost.
     * @param k The maximum number of teleportations allowed.
     * @return The minimum cost to reach the bottom-right corner, or -1 if it's not reachable.
     */
    public int minCost(int[][] grid, int k) {
        int m = grid.length;
        int n = grid[0].length;
        int maxVal = 0;

        for (int[] row : grid) {
            for (int val : row) {
                maxVal = Math.max(maxVal, val);
            }
        }

        boolean[] present = new boolean[maxVal + 1];
        for (int[] row : grid) {
            for (int val : row) {
                present[val] = true;
            }
        }

        List<Integer> distinctVals = new ArrayList<>();
        int[] valToIdx = new int[maxVal + 1];
        Arrays.fill(valToIdx, -1);

        for (int i = 0; i <= maxVal; i++) {
            if (present[i]) {
                valToIdx[i] = distinctVals.size();
                distinctVals.add(i);
            }
        }

        int numDistinct = distinctVals.size();
        List<int[]>[] coordsByIndex = new ArrayList[numDistinct];
        for (int i = 0; i < numDistinct; i++) {
            coordsByIndex[i] = new ArrayList<>();
        }

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                int idx = valToIdx[grid[r][c]];
                coordsByIndex[idx].add(new int[]{r, c});
            }
        }

        int[][][] dist = new int[k + 1][m][n];
        for (int i = 0; i <= k; i++) {
            for (int j = 0; j < m; j++) {
                Arrays.fill(dist[i][j], Integer.MAX_VALUE);
            }
        }

        int[][] distVirt = new int[k + 1][numDistinct];
        for (int i = 0; i <= k; i++) {
            Arrays.fill(distVirt[i], Integer.MAX_VALUE);
        }

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));

        dist[0][0][0] = 0;
        pq.offer(new int[]{0, 0, 0, 0});

        int[] dr = {0, 1};
        int[] dc = {1, 0};

        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int d = curr[0];
            int r = curr[1];
            int c = curr[2];
            int moves = curr[3];

            if (r == -1) {
                int vIdx = c;
                if (d > distVirt[moves][vIdx]) {
                    continue;
                }

                if (vIdx > 0) {
                    int nextVIdx = vIdx - 1;
                    if (distVirt[moves][nextVIdx] > d) {
                        distVirt[moves][nextVIdx] = d;
                        pq.offer(new int[]{d, -1, nextVIdx, moves});
                    }
                }

                for (int[] pos : coordsByIndex[vIdx]) {
                    int tr = pos[0];
                    int tc = pos[1];
                    if (dist[moves][tr][tc] > d) {
                        dist[moves][tr][tc] = d;
                        pq.offer(new int[]{d, tr, tc, moves});
                    }
                }
            } else {
                if (d > dist[moves][r][c]) {
                    continue;
                }
                if (r == m - 1 && c == n - 1) {
                    return d;
                }

                for (int i = 0; i < 2; i++) {
                    int nr = r + dr[i];
                    int nc = c + dc[i];

                    if (nr < m && nc < n) {
                        int newCost = d + grid[nr][nc];
                        if (newCost < dist[moves][nr][nc]) {
                            dist[moves][nr][nc] = newCost;
                            pq.offer(new int[]{newCost, nr, nc, moves});
                        }
                    }
                }

                if (moves < k) {
                    int val = grid[r][c];
                    int vIdx = valToIdx[val];
                    if (distVirt[moves + 1][vIdx] > d) {
                        distVirt[moves + 1][vIdx] = d;
                        pq.offer(new int[]{d, -1, vIdx, moves + 1});
                    }
                }
            }
        }

        return -1;
    }
}