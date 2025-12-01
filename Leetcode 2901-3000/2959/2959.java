// Leetcode 2959: Number of Possible Sets of Closing Branches
// https://leetcode.com/problems/number-of-possible-sets-of-closing-branches/
// Solved on 1st of December, 2025
import java.util.Arrays;

class Solution {
    /**
     * Calculates the number of possible sets of closing branches such that the maximum distance
     * between any two remaining branches is at most `maxDistance`.
     *
     * @param n The total number of branches.
     * @param maxDistance The maximum allowed distance between any two remaining branches.
     * @param roads A 2D array where each `roads[i] = [u, v, w]` represents a road between branch `u` and branch `v` with distance `w`.
     * @return The number of valid sets of closing branches.
     */
    public int numberOfSets(int n, int maxDistance, int[][] roads) {
        int ans = 0;
        int[][] adj = new int[n][n];
        int[][] d = new int[n][n];
        int inf = 1000000000;

        for (int i = 0; i < n; i++) {
            Arrays.fill(adj[i], inf);
            adj[i][i] = 0;
        }

        for (int[] road : roads) {
            int u = road[0];
            int v = road[1];
            int w = road[2];
            adj[u][v] = Math.min(adj[u][v], w);
            adj[v][u] = Math.min(adj[v][u], w);
        }

        for (int mask = 0; mask < (1 << n); mask++) {
            for (int i = 0; i < n; i++) {
                if (((mask >> i) & 1) == 1) {
                    for (int j = 0; j < n; j++) {
                        if (((mask >> j) & 1) == 1) {
                            d[i][j] = adj[i][j];
                        }
                    }
                }
            }

            for (int k = 0; k < n; k++) {
                if (((mask >> k) & 1) == 1) {
                    for (int i = 0; i < n; i++) {
                        if (((mask >> i) & 1) == 1) {
                            for (int j = 0; j < n; j++) {
                                if (((mask >> j) & 1) == 1) {
                                    d[i][j] = Math.min(d[i][j], d[i][k] + d[k][j]);
                                }
                            }
                        }
                    }
                }
            }

            boolean valid = true;
            for (int i = 0; i < n; i++) {
                if (((mask >> i) & 1) == 1) {
                    for (int j = 0; j < n; j++) {
                        if (((mask >> j) & 1) == 1) {
                            if (d[i][j] > maxDistance) {
                                valid = false;
                                break;
                            }
                        }
                    }
                    if (!valid) break;
                }
            }

            if (valid) {
                ans++;
            }
        }
        return ans;
    }
}