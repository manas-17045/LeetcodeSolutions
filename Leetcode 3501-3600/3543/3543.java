// Leetcode 3543: Maximum Weighted K-Edge path
// https://leetcode.com/problems/maximum-weighted-k-edge-path/
// Solved on 2nd of November, 2025
class Solution {
    /**
     * Calculates the maximum weight of a k-edge path in a graph.
     * @param n The number of nodes in the graph.
     * @param edges A 2D array representing the edges, where edges[i] = [u, v, w] means an edge from u to v with weight w.
     * @param k The number of edges in the path.
     * @param t The maximum allowed total weight for a path.
     * @return The maximum weight of a k-edge path that does not exceed t, or -1 if no such path exists.
     */
    public int maxWeight(int n, int[][] edges, int k, int t) {
        boolean[][] dp = new boolean[n][t];
        for (int i = 0; i < n; i++) {
            dp[i][0] = true;
        }

        for (int i = 0; i < k; i++) {
            boolean[][] nextDp = new boolean[n][t];
            boolean hasPath = false;
            for (int[] edge : edges) {
                int u = edge[0];
                int v = edge[1];
                int w = edge[2];
                if (w >= t) {
                    continue;
                }
                for (int val = 0; val < t - w; val++) {
                    if (dp[u][val]) {
                        nextDp[v][val + w] = true;
                        hasPath = true;
                    }
                }
            }
            if (!hasPath) {
                return -1;
            }
            dp = nextDp;
        }

        int max = -1;
        for (int i = 0; i < n; i++) {
            for (int val = t - 1; val >= 0; val--) {
                if (dp[i][val]) {
                    if (val > max) {
                        max = val;
                    }
                    break;
                }
            }
        }
        return max;
    }
}