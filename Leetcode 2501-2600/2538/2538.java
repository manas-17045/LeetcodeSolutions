// Leetcode 2538: Difference Between Maximum and Minimum Price Sum
// https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/
// Solved on 11th of December, 2025
import java.util.*;

class Solution {
    private List<Integer>[] adj;
    private long[] prices;
    private long[] maxPathSumDown;
    private long maxCost;

    /**
     * Given a tree with `n` nodes and their `prices`, find the maximum difference between the sum of prices
     * along two paths starting from different nodes and ending at different nodes.
     * @param n The number of nodes in the tree.
     * @param edges An array of edges representing the connections between nodes.
     * @param price An array of prices for each node.
     * @return The maximum difference between the sum of prices of two paths.
     */
    public long maxOutput(int n, int[][] edges, int[] price) {
        if (n == 1) {
            return 0;
        }

        prices = new long[n];
        for (int i = 0; i < n; i++) {
            prices[i] = price[i];
        }

        adj = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new ArrayList<>();
        }

        for (int[] edge : edges) {
            adj[edge[0]].add(edge[1]);
            adj[edge[1]].add(edge[0]);
        }

        maxPathSumDown = new long[n];
        maxCost = 0;

        dfsDown(0, -1);
        dfsUp(0, -1, 0);

        return maxCost;
    }

    private long dfsDown(int u, int p) {
        long max = 0;
        for (int v : adj[u]) {
            if (v == p) {
                continue;
            }
            max = Math.max(max, dfsDown(v, u));
        }
        maxPathSumDown[u] = max + prices[u];
        return maxPathSumDown[u];
    }

    private void dfsUp(int u, int p, long maxFromParent) {
        long maxPathStartAtU = Math.max(maxPathSumDown[u], maxFromParent + prices[u]);
        maxCost = Math.max(maxCost, maxPathStartAtU - prices[u]);

        long m1 = 0;
        long m2 = 0;
        for (int v : adj[u]) {
            if (v == p) {
                continue;
            }
            long val = maxPathSumDown[v];
            if (val > m1) {
                m2 = m1;
                m1 = val;
            } else if (val > m2) {
                m2 = val;
            }
        }

        for (int v : adj[u]) {
            if (v == p) {
                continue;
            }
            long siblingMax = (maxPathSumDown[v] == m1) ? m2 : m1;
            long newMaxFromParent = Math.max(maxFromParent, siblingMax) + prices[u];
            dfsUp(v, u, newMaxFromParent);
        }
    }
}